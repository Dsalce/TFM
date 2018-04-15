#Comandos py.exe setup.py build
#Copiar la carpeta images y los dll tcl86t.dll,tk86t.dll al build(borrar los anteriores)

import sys
from cx_Freeze import setup, Executable
from sys import path
import tkinter
import os

os.environ['TCL_LIBRARY'] = "C:\\Program Files (x86)\\Microsoft Visual Studio\\Shared\\Python36_64\\DLLs\\tcl86t.dll"
os.environ['TK_LIBRARY'] = "C:\\Program Files (x86)\\Microsoft Visual Studio\\Shared\\Python36_64\\DLLs\\tk86t.dll"



additional_mods = ['numpy.core._methods', 'numpy.lib.format','matplotlib.backends.backend_tkagg','tkinter','tkinter.filedialog']
setup(
      version='1.0',
	  options = {'build_exe': {'includes': additional_mods}},
	  windows = [{"icon_resources": [(1, "D:\David_inf\TFM\Image\icon.ico")]}],
      executables = [Executable('Model/DeteccionAnomaliasItv.py',base = "Win32GUI")])
	  
	  