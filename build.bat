rmdir /s /q dist
pyinstaller --add-data "assets/icon.ico;." -i "assets/icon.ico" --noupx --windowed --onedir mike.py
