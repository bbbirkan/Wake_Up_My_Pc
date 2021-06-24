
from setuptools import setup

APP = ['Wake.py']
DATA_FILES = ["DataSave.pkl"]
OPTIONS = {'argv_emulation': True,'packages': ['pickle',"wakeonlan"]}
APP_NAME="WakeUp PC"

setup(
    name=APP_NAME,
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
