from cx_Freeze import setup, Executable
import os
import sys

'''
PYTHON_INSTALL_DIR = os.path.dirname(sys.executable)
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')

build_exe_options = {'include_files': [(os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tk86t.dll'),
                                        os.path.join('lib', 'tk86t.dll')),
                                       (os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tcl86t.dll'),
                                        os.path.join('lib', 'tcl86t.dll'))]}

'''

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

exe = Executable(
      script="Jeu_test_prix_Maubert.py",
      base=base,
      targetName="Jeu_test_prix_Maubert.exe"
     )

setup(
      name="QuizzMAUBERT.exe",
      version="0.1",
      author="Amandine Sandri",
      description="Devinez les prix du Menu MAUBERT / Copyright 2019",
      #options = {"build_exe": build_exe_options},
      executables=[exe]
      )
