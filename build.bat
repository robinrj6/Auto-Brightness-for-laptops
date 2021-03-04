pyinstaller adaptive.py -F --noconsole
pyinstaller .\ui.py -F --noconsole --add-binary "./dist/adaptive.exe;./adaptive"