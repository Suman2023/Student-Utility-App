# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['app.py'],
             pathex=['C:\\Users\\home\\Desktop\\All\\Python\\Student Utility App'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)


# -*- file location below to be changed with your path -*-

a.datas += [('wikipedia.png','C:\\Users\\home\\Desktop\\All\\Python\\Student Utility App\\Images\\wikipedia.png', "DATA")]
a.datas += [('calculator.png','C:\\Users\\home\\Desktop\\All\\Python\\Student Utility App\\Images\\calculator.png', "DATA")]
a.datas += [('todo.png','C:\\Users\\home\\Desktop\\All\\Python\\Student Utility App\\Images\\todo.png', "DATA")]
a.datas += [('music.png','C:\\Users\\home\\Desktop\\All\\Python\\Student Utility App\\Images\\music.png', "DATA")]
a.datas += [('jazz.png','C:\\Users\\home\\Desktop\\All\\Python\\Student Utility App\\Images\\jazz.png', "DATA")]

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='app',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
