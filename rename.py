import os
import webbrowser
from tkinter import filedialog,simpledialog
import tkinter
import win32gui, win32com.client

gui = tkinter.Tk()
gui.title("Rename")
fileDir = tkinter.filedialog.askdirectory()
hwnd = win32gui.FindWindow(0,"Rename")
i = 0
c = 1

for filename in os.listdir(fileDir):
    webbrowser.open_new(fileDir + "/" + filename)
    shell = win32com.client.Dispatch("WScript.Shell")
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(hwnd)
    title = str(c) + "/" + str(len(os.listdir(fileDir)))
    newName = tkinter.simpledialog.askstring(title,"Enter contract number (Enter 0 to skip): ")
    c+=1
    if newName == "0":
        os.rename(fileDir + "/" + filename,fileDir + "/0-junkfile" + str(i) + ".pdf")
        i+=1
    else:
        os.rename(fileDir + "/" + filename,fileDir + "/Contract}U}" + newName + "}U}OT}I}Scanned_copy.pdf")