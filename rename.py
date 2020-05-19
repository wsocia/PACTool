import os
import webbrowser
from tkinter import filedialog,simpledialog
import win32gui

fileDir = filedialog.askdirectory()
handle = win32gui.FindWindow(0, "tk")
i = 0

for filename in os.listdir(fileDir):
    webbrowser.open_new(fileDir + "/" + filename)
    win32gui.SetForegroundWindow(handle)
    newName = simpledialog.askstring("Contract Rename Tool","Enter contract number (Enter 0 to skip): ")
    if newName == "0":
        os.rename(fileDir + "/" + filename,fileDir + "/0-junkfile" + str(i) + ".pdf")
        i+=1
    else:
        os.rename(fileDir + "/" + filename,fileDir + "/Contract}U}" + newName + "}U}OT}I}Scanned_copy.pdf")