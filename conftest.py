"""
Shared pytest bootstrap for repository-wide test execution.

This makes the legacy tests under simulator/ importable from the project root,
which is the execution mode expected by SonarQube coverage collection in CI.
"""
from pathlib import Path
from uuid import uuid4
import os
import sys

import pytest


PROJECT_ROOT = Path(__file__).resolve().parent
SIMULATOR_DIR = PROJECT_ROOT / "simulator"

# Keep relative test fixtures and assets stable no matter where pytest is started.
os.chdir(PROJECT_ROOT)

for candidate in (str(PROJECT_ROOT), str(SIMULATOR_DIR)):
    if candidate not in sys.path:
        sys.path.insert(0, candidate)


@pytest.fixture
def tmp_path():
    """Project-local replacement for pytest's tmp_path fixture.

    The default pytest temp root is not reliable in this environment, so we
    create a temporary directory under the repository's temp/ folder instead.
    """
    temp_root = PROJECT_ROOT / "temp" / "pytest-fixtures"
    temp_root.mkdir(parents=True, exist_ok=True)
    path = temp_root / f"tmp-{uuid4().hex}"
    path.mkdir()
    yield path
