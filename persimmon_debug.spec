# -*- mode: python -*-

from kivy.deps import sdl2, angle#, glew
from PyInstaller.utils.hooks import collect_submodules

from glob import iglob
from itertools import chain
from os.path import dirname
import pathlib


non_py_files = chain.from_iterable(
	(iglob('**/*.{}'.format(ext), recursive=True) for ext in ['kv', 'png']))

non_py_files = [(file, dirname(file)) for file in non_py_files]


block_cipher = None

a = Analysis(['persimmon\\__main__.py'],
             pathex=['.\\persimmon'],
             binaries=None,
             datas=non_py_files,
	     hiddenimports=collect_submodules('scipy') + collect_submodules('sklearn') + ['win32timezone'],
             hookspath=[],
             runtime_hooks=[],
             excludes=['jinja2.asyncsupport','jinja2.asyncfilters'],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='persimmon_debug',
          debug=False,
          strip=False,
          upx=True,
          console=True)

coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               *[Tree(p) for p in (sdl2.dep_bins + angle.dep_bins)], #+ glew.dep_bins)],
               strip=False,
               upx=True,
               name='persimmon_debug')
