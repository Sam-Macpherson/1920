"""Setup script for 1920"""

import os.path
import sys

from cx_Freeze import setup, Executable

# The directory containing this file
HERE = os.path.abspath(os.path.dirname(__file__))

# The text of the README file
with open(os.path.join(HERE, "README.md")) as fid:
    README = fid.read()

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="1920",
    version="0.1",
    description="Game about twirling pizzas and selling alcohol.",
    executables=[Executable("main.py", base=base)]
)
