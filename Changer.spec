# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['Changer.py'],
             pathex=[],
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
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

a.datas += [('Eagle_33892.ico','C:\\Users\\User\\Desktop\\SettingsChanger\\Eagle_33892.ico', "DATA")]
a.datas += [('bg.png','C:\\Users\\User\\Desktop\\SettingsChanger\\bg.png', "DATA")]
a.datas += [('dc.png','C:\\Users\\User\\Desktop\\SettingsChanger\\dc.png', "DATA")]

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,  
          [],
          name='Changer',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )
