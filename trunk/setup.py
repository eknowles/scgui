#!/usr/bin/python
import sys
from distutils.core import setup
import py2exe
from glob import glob

data_files = [("Microsoft.VC90.CRT", glob(r'C:\Windows\winsxs\x86_microsoft.vc90.crt_1fc8b3b9a1e18e3b_9.0.30729.6161_none_50934f2ebcb7eb57\*.*'))]
setup(
    data_files=data_files,
    windows = [
        {
            "script": "main.py",
            "icon_resources": [(1, "counterstrike-5.ico")]
        }
    ],
    options={"py2exe": {"includes": ["sip", "PyQt4.QtGui", "PyQt4.QtNetwork"]}}
)
