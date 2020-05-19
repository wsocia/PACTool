import os
import webbrowser
from tkinter import filedialog,simpledialog
import tkinter
import win32gui

gui = tkinter.Tk()
gui.title("Rename")
fileDir = filedialog.askdirectory()
i = 0

for filename in os.listdir(fileDir):
    webbrowser.open_new(fileDir + "/" + filename)
    handle = win32gui.FindWindow(None, "Rename")
    win32gui.SetForegroundWindow(handle)
    newName = simpledialog.askstring("Contract Rename Tool","Enter contract number (Enter 0 to skip): ")
    if newName == "0":
        os.rename(fileDir + "/" + filename,fileDir + "/0-junkfile" + str(i) + ".pdf")
        i+=1
    else:
        os.rename(fileDir + "/" + filename,fileDir + "/Contract}U}" + newName + "}U}OT}I}Scanned_copy.pdf")