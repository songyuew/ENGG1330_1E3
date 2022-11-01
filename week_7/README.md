# Pack Python File to Executable

1. Install `PyInstaller` module

```
pip install PyInstaller
```

2. Pack to executable
```
python -m PyInstaller -F <PATH_TO_PY>
```

Note: If you want to prepare executable for Windows, you must pack your codes on a Windows machine. If you want the program to run on Mac/Linux, then you have to operate on a Unix machine.
