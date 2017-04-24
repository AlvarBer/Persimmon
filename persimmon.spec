# -*- mode: python -*-

from kivy.deps import sdl2, glew
from PyInstaller.utils.hooks import collect_submodules

from glob import glob
from os.path import dirname
import pathlib


kv_files = glob('**/*.kv', recursive=True) 

non_python_files = []
for file in kv_files:
	non_python_files.append((file,
	       str(pathlib.Path(*pathlib.Path(dirname(file)).parts[1:]))))
block_cipher = None

non_python_files.append(('persimmon/connections.png', '.'))

a = Analysis(['persimmon\\__main__.py'],
             pathex=['persimmon'],
             binaries=None,
             datas=non_python_files,
             hiddenimports=collect_submodules('scipy') + collect_submodules('sklearn') + ['win32timezone'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
	  *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],
          name='persimmon',
          debug=False,
          strip=False,
          upx=True,
          console=False)
