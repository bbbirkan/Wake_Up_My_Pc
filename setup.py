from setuptools import setup

APP = ['WakeUp_Mac.py']
DATA_FILES = ["data_save_control.pkl"]
OPTIONS = {'argv_emulation': False,'packages': ['pickle',"time","tkinter","wakeonlan"]}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
