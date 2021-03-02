import sys
import os
from tkinter import *
import subprocess

window=Tk()
window.title("Adaptive Brightness")
window.geometry('200x200')

def run():
    subprocess.call([r'run.bat'])

def stop():
    os.system("taskkill /IM pythonw.exe /F")

btn1 = Button(window, text="Run",command=run).place(x=90, y=50)
btn2 = Button(window, text="Stop",command=stop).place(x=90, y=150)

window.mainloop()