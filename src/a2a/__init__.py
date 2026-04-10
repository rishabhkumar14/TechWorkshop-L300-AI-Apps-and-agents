"""Zava A2A Agent package."""
import sys
from pathlib import Path

# Ensure the installed a2a package (from a2a-sdk) is accessible
# by removing the parent directory from sys.path[0] if it's there
_parent_dir = str(Path(__file__).parent.parent)
if sys.path and sys.path[0] == _parent_dir:
    sys.path.pop(0)
    sys.path.append(_parent_dir)

__version__ = "1.0.0"
