from tkinter import *
from tkinter import filedialog

def renameFile():
	newFile = entry1.get()
	os.rename(fileIn, filePathDest + "/" + newFile + ".pdf")
	entry1.set()
	
def setPathSource():
	f = open("config.ini","w")
	filePathSource = filedialog.askdirectory()
	labelSourceText.set(filePathSource)
	f.writelines(filePathSource)
	f.close

def setPathDest():
	filePathDir = filedialog.askdirectory()
	labelOutText.set(filePathDest)

def getPathDir():
	f = open("config.ini","r")
	filePathSource = f.readline()
	filePathDest = f.readline()
	f.close

def drawGUI():	
	guiWindow = Tk()
	guiWindow.title("Contract Rename Tool")
	guiWindow.geometry("400x100")

	buttonSource=Button(guiWindow,text="Select Source Directory",command=setPathSource)
	buttonSource.grid(row=0,column=0)
	labelSourceText = StringVar()
	labelSourceText.set(filePathSource)
	labelSource=Label(guiWindow,textvariable=labelSourceText)
	labelSource.grid(row=0, column=1)

	buttonOut=Button(guiWindow,text="Select Output Directory",command=setPathDest)
	buttonOut.grid(row=1,column=0)
	labelOutText = StringVar()
	labelOutText.set(filePathDest)
	labelOut=Label(guiWindow,textvariable=labelOutText)
	labelOut.grid(row=1, column=1)

	label1=Label(guiWindow,text="Enter contract number:")
	label1.grid(row=2,column=0)

	entry1=Entry(guiWindow)
	entry1.grid(row=2,column=1)

	button2=Button(guiWindow,text="Submit",command=renameFile)
	button2.grid(row=2,column=2)
	guiWindow.bind('<Return>',renameFile)

	guiWindow.mainloop()
