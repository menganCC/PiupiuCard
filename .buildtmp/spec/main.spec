# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['E:\\code\\py\\.buildtmp\\_main.py'],
    pathex=['E:\\code\\py\\.buildtmp'],
    binaries=[('E:\\code\\py\\.buildtmp\\main.cp313-win_amd64.pyd', '.')],
    datas=[('E:\\code\\py\\.buildtmp\\ui\\dist', 'ui\\dist'), ('E:\\code\\py\\.buildtmp\\default.png', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=['E:\\code\\py\\.buildtmp\\_pyi_rth_system_runtime.py'],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['C:\\Users\\20975\\Downloads\\jdpdf-7rqcu-001.ico'],
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='main',
)
