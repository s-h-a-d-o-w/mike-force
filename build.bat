rmdir /s /q dist
pyinstaller --add-data "icon.ico;." -i "icon.ico" --splash "icon.ico" --noupx --windowed --onefile mike.py
