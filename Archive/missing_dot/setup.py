from distutils.core import setup
import py2exe

import sys
sys.argv.append("py2exe")

py2exe_options = dict(
    excludes = ["doctest", "inspect", "pdb", "unittest", "difflib", "inspect", "multiprocessing", "locale", "asyncio", "pyreadline",
                "matplotlib"], 
    dll_excludes = ['msvcr71.dll'],
    compressed = True
)

setup(name = "Missing Dot",
    author = "Helly",
    console = ["missing_dot.py", "dot_setup.py", "info.py"],
    options = {"py2exe": py2exe_options},
    description = "Simple game"
    )