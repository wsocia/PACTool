import os
import webbrowser
from tkinter import filedialog,simpledialog
import win32gui
import time

fileDir = filedialog.askdirectory()
hwnd = win32gui.FindWindow(None, "tk")
i = 0

for filename in os.listdir(fileDir):
    webbrowser.open_new(fileDir + "/" + filename)
    time.sleep(.5)
    win32gui.SetForegroundWindow(hwnd)
    newName = simpledialog.askstring("Rename","Enter contract number (Enter 0 to skip): ")
    if newName == "0":
        os.rename(fileDir + "/" + filename,fileDir + "/0-junkfile" + str(i) + ".pdf")
        i+=1
    else:
        os.rename(fileDir + "/" + filename,fileDir + "/Contract}U}" + newName + "}U}OT}I}Scanned_copy.pdf")