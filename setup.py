from setuptools import setup

APP = ["app.py"]
DATA_FILES = [
    ("assets", ["assets/icon.png", "assets/App.icns"])
]
OPTIONS = {
    "iconfile": "assets/App.icns",
    "plist": {
        "LSUIElement": True,
        "CFBundleName": "Breather",
        "CFBundleDisplayName": "Breather",
        "CFBundleIdentifier": "com.yourname.breather.v2",
        "CFBundleVersion": "0.1.0",
        "CFBundleShortVersionString": "0.1.0",
        "NSHumanReadableCopyright": "Copyright © 2026",
    },
    "argv_emulation": False,
    "packages": ["rumps"],
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={"py2app": OPTIONS},
    setup_requires=["py2app"],
)