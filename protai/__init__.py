import sys
import os

sys.path.append(os.path.dirname(__file__))

# Attempt to read the version from VERSION file
version_file_path = os.path.join(
    os.path.abspath(os.path.dirname(__file__)), "VERSION"
)
default_version = "0.0.0"


def read_version(version_file_path) -> str:
    try:
        with open(version_file_path, "r") as version_file:
            return version_file.read().strip()
    except FileNotFoundError:
        return default_version  # Default version if not found
    except Exception:
        return default_version


__version__ = read_version(version_file_path)
