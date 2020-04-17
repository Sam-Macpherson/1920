"""Setup script for 1920"""

import sys

from cx_Freeze import setup, Executable


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
