from __future__ import annotations

import os
import shutil
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import Any, ClassVar, Dict, List

from isolate.backends import BaseEnvironment, EnvironmentCreationError
from isolate.backends.common import (
    cache_static,
    logged_io,
    rmdir_on_fail,
    sha256_digest_of,
)
from isolate.backends.connections import PythonIPC
from isolate.backends.context import GLOBAL_CONTEXT, ContextType

# Specify the path where the conda binary might reside in (or
# mamba, if it is the preferred one).
_CONDA_COMMAND = os.environ.get("CONDA_EXE", "conda")
_ISOLATE_CONDA_HOME = os.getenv("ISOLATE_CONDA_HOME")


@dataclass
class CondaEnvironment(BaseEnvironment[Path]):
    BACKEND_NAME: ClassVar[str] = "conda"

    packages: List[str]

    @classmethod
    def from_config(
        cls,
        config: Dict[str, Any],
        context: ContextType = GLOBAL_CONTEXT,
    ) -> BaseEnvironment:
        user_provided_packages = config.get("packages", [])
        environment = cls(user_provided_packages)
        environment.set_context(context)
        return environment

    @property
    def key(self) -> str:
        return sha256_digest_of(*self.packages)

    def create(self) -> Path:
        path = self.context.get_cache_dir(self) / self.key
        if path.exists():
            return path

        with rmdir_on_fail(path):
            self.log(f"Creating the environment at '{path}'")
            conda_executable = _get_conda_executable()
            if self.packages:
                self.log(f"Installing packages: {', '.join(self.packages)}")

            with logged_io(self.log) as (stdout, stderr):
                try:
                    subprocess.check_call(
                        [
                            conda_executable,
                            "create",
                            "--yes",
                            # The environment will be created under $BASE_CACHE_DIR/conda
                            # so that in the future we can reuse it.
                            "--prefix",
                            path,
                            *self.packages,
                        ],
                        stdout=stdout,
                        stderr=stderr,
                    )
                except subprocess.SubprocessError as exc:
                    raise EnvironmentCreationError(
                        "Failure during 'conda create'"
                    ) from exc

        return path

    def destroy(self, connection_key: Path) -> None:
        shutil.rmtree(connection_key)

    def exists(self) -> bool:
        path = self.context.get_cache_dir(self) / self.key
        return path.exists()

    def open_connection(self, connection_key: Path) -> PythonIPC:
        return PythonIPC(self, connection_key)


@cache_static
def _get_conda_executable() -> Path:
    for path in [_ISOLATE_CONDA_HOME, None]:
        conda_path = shutil.which(_CONDA_COMMAND, path=path)
        if conda_path is not None:
            return Path(conda_path)
    else:
        # TODO: we should probably show some instructions on how you
        # can install conda here.
        raise FileNotFoundError(
            "Could not find conda executable. If conda executable is not available by default, please point isolate "
            " to the path where conda binary is available 'ISOLATE_CONDA_HOME'."
        )
