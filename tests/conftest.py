"""Test config"""

from pathlib import Path
from tempfile import TemporaryDirectory

import pytest


@pytest.fixture
def mock_path() -> Path:
    """Mock a path, and clean when unit test done."""
    temp_path = TemporaryDirectory()
    yield Path(temp_path.name)
    temp_path.cleanup()
