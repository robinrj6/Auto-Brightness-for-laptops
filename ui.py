import os
import sys
from tkinter import *
import subprocess

window = Tk()
window.title("Adaptive Brightness")
window.geometry('200x200')


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(__file__)
    return os.path.join(base_path, relative_path)


def run():
    subprocess.Popen([resource_path('main.exe')])


def stop():
    os.system("taskkill /IM main.exe /F")


btn1 = Button(window, text="Run", command=run).place(x=90, y=50)
btn2 = Button(window, text="Stop", command=stop).place(x=90, y=150)

window.mainloop()
