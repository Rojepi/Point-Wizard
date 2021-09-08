# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['point_wizard.py'],
             pathex=['E:\\Documents\\PRGM\\point_wizard'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
a.datas += [('point_wizard_name_0.txt', 'E:\\Documents\\PRGM\\point_wizard\\point_wizard_name_0.txt', 'DATA'),('point_wizard_name_1.txt', 'E:\\Documents\\PRGM\\point_wizard\\point_wizard_name_1.txt', 'DATA'),('point_button.jpg', 'E:\\Documents\\PRGM\\point_wizard\\point_button.jpg', 'DATA')]
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,  
          [],
          name='point_wizard',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None,
          icon='E:\\Documents\\PRGM\\point_wizard\\icon-s.ico' )
