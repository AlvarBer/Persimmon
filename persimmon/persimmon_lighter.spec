# -*- mode: python -*-

from kivy.deps import sdl2, glew
from PyInstaller.utils.hooks import collect_submodules


block_cipher = None
flatten = lambda l: [item for sublist in l for item in sublist]

a = Analysis(['__main__.py'],
             pathex=['C:\\Users\\Mortadelegle\\Code\\Persimmon\\persimmon'],
             binaries=None,
             datas=[('view/test.kv', 'persimmon/view')],
             hiddenimports=collect_submodules('scipy') + flatten([collect_submodules(module) for module in ['sklearn.svm', 'sklearn.ensemble', 'sklearn.model_selection', 'sklearn.neighbors']]) + ['kivy.uix.filechooser'],
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
          console=True)
