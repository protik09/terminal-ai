#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Note: To use the 'upload' functionality of this file, you must:
#   $ pipenv install twine --dev

import io
import os
import sys
from shutil import rmtree

from setuptools import find_packages, setup, Command

# Open requirements.txt and read file into a list of strings
with open("requirements.txt", "r") as file:
    requirements = file.read().splitlines()

# Package meta-data.
NAME = "protai"
DESCRIPTION = "A useful 0-Shot AI in the terminal"
EMAIL = "protik09@users.noreply.github.com"
URL = "https://github.com/protik09/terminal-ai"
AUTHOR = "Protik Banerji"
REQUIRES_PYTHON = ">=3.10.0"

# Attempt to read the version from VERSION file
version_file_path = os.path.join(
    os.path.abspath(os.path.dirname(__file__)), "protai", "VERSION"
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


VERSION = read_version(version_file_path)

# What packages are required for this module to be executed?
REQUIRED = requirements

# What packages are optional?
EXTRAS: dict = {
    # 'fancy feature': ['django'],
}

# The rest you shouldn't have to touch too much :)
# ------------------------------------------------
# Except, perhaps the License and Trove Classifiers!
# If you do change the License, remember to change the Trove Classifier for that!

here = os.path.abspath(os.path.dirname(__file__))

# Import the README and use it as the long-description.
# Note: this will only work if 'README.md' is present in your MANIFEST.in file!
try:
    with io.open(os.path.join(here, "README.md"), encoding="utf-8") as f:
        long_description = "\n" + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION


class UploadCommand(Command):
    """Support setup.py upload."""

    description = "Build and publish the package."
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print("\033[1m{0}\033[0m".format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status("Removing previous builds…")
            rmtree(os.path.join(here, "dist"))
        except OSError:
            pass

        self.status("Building Source and Wheel (universal) distribution…")
        os.system("{0} setup.py sdist bdist_wheel --universal".format(sys.executable))

        self.status("Uploading the package to PyPI via Twine…")
        os.system("twine upload dist/*")  # Upload directly to main PyPi
        # os.system("twine upload --repository testpypi dist/*")  # Upload to test PyPi

        self.status("Pushing git tags…")
        os.system("git tag v{0}".format(VERSION))
        os.system("git push --tags")

        sys.exit()


# Where the magic happens:
setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(exclude=["tests", "*.tests", "*.tests.*", "tests.*"]),
    entry_points={
        "console_scripts": ["protai=protai.protai:main"],
    },
    install_requires=REQUIRED,
    extras_require=EXTRAS,
    include_package_data=True,
    package_data={
        "protai": ["VERSION"],  # Include the VERSION file
    },
    license="MIT",
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    # $ setup.py publish support.
    cmdclass={
        "upload": UploadCommand,
    },
)
