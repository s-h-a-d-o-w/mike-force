rmdir /s /q dist
pyinstaller --add-data "assets/icon.ico;assets" -i "assets/icon.ico" --noupx --windowed --onedir mike.py
del dist\mike\PyQt5\Qt5\bin\opengl32sw.dll
del dist\mike\PyQt5\Qt5\bin\d3dcompiler_47.dll
