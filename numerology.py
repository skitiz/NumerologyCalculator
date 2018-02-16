from distutils.core import setup
from glob import glob
import py2exe

data_files = [("Microsoft.VC90.CRT", glob(r'C:\Program Files\Microsoft Visial Studio 9.0\VC\redist\x86\Microsoft.VC90.CRT\*.*'))]
setup (
    data_files = data_files
)
setup(console=['number.py'])
