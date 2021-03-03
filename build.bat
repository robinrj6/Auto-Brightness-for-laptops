pyinstaller main.py -F --noconsole
pyinstaller .\ui.py -F --noconsole --add-binary "./dist/main.exe;./main"