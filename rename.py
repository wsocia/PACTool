import os
import webbrowser
from tkinter import filedialog,simpledialog
import win32gui

fileDir = filedialog.askdirectory()
handle = win32gui.FindWindow(0, "tk")

for filename in os.listdir(fileDir):
    webbrowser.open_new(fileDir + "/" + filename)
    win32gui.SetForegroundWindow(handle)
    newName = simpledialog.askstring("Contract Rename Tool","Enter contract number (Enter 0 to delete): ")
    if newName == "0":
        os.remove(fileDir + "/" + filename)
    else:
        os.rename(fileDir + "/" + filename,fileDir + "/" + newName + ".pdf")