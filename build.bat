rmdir /s /q dist
pyinstaller --add-data "icon.ico;." -i "icon.ico" --noupx --windowed --onedir mike.py
