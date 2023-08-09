import tkinter as tk
from tkinter import filedialog
import customtkinter as ct
from saveGraphicsPath import saveGraphicsPath, loadGraphicsPath

class GraphicsFolderFrame(ct.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.fmPathHeading = ct.CTkLabel(self, text="STEP 1")
        self.fmPathHeading.pack(padx=0, pady=5)
        self.fmPathLabel = ct.CTkLabel(self, text="Select Football Manager Graphics Folder Path", fg_color="gray30", corner_radius=6)
        self.fmPathLabel.pack(padx=20, pady=3)
        self.inputButton = ct.CTkButton(self, text="Browse", command=self.findFolder)
        self.inputButton.pack(padx=20, pady=20)
        self.lastButton = ct.CTkButton(self, text="Load Last Folder", command=self.getLastPath)
        self.lastButton.pack(padx=20, pady=20)
        self.filePathLabel = ct.CTkLabel(self, text="Folder Path Picked:")
        self.filePathLabel.pack()
        self.filePathPath = ct.CTkLabel(self, text="")
        self.filePathPath.pack()

    def getLastPath(self):
        self.path = loadGraphicsPath()
        self.filePathPath.configure(text=self.path)

    # Add FootballManager Path
    def findFolder(self):
        self.filePath = filedialog.askdirectory()
        self.filePathPath.configure(text=self.filePath)

class ImportTypeFrame(ct.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.fmPathHeading = ct.CTkLabel(self, text="STEP 2")
        self.fmPathHeading.pack(padx=0, pady=5)
        self.fmPathLabel = ct.CTkLabel(self, text="Select Import Type", fg_color="gray30", corner_radius=6)
        self.fmPathLabel.pack(padx=20, pady=3)

        self.importTypeVar = ct.StringVar()
        self.importTypeVar.set("logo") 
        self.logoRadioButton = ct.CTkRadioButton(self, text="Team Logo Import", variable=self.importTypeVar, value="logo")
        self.logoRadioButton.pack(padx=20, pady=3)
        self.playerRadioButton = ct.CTkRadioButton(self, text="Player Image Import", variable=self.importTypeVar, value="player")
        self.playerRadioButton.pack(padx=20, pady=15)

class UploadImageFrame(ct.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.fmPathHeading = ct.CTkLabel(self, text="STEP 3")
        self.fmPathHeading.pack(padx=0, pady=5)
        self.fmPathLabel = ct.CTkLabel(self, text="Select Image to Import" , fg_color="gray30", corner_radius=6)
        self.fmPathLabel.pack(padx=20, pady=3)
        self.inputButton = ct.CTkButton(self, text="Browse", command=self.findFolder)
        self.inputButton.pack(padx=20, pady=20)
        self.filePathLabel = ct.CTkLabel(self, text="File Picked:")
        self.filePathLabel.pack(padx=10, pady=10)
        self.imagePathLabel = ct.CTkLabel(self, text="")
        self.imagePathLabel.pack(padx=10, pady=10)

    # Import Image
    def findFolder(self):
        self.filePath = filedialog.askopenfilename()
        self.imagePathLabel.configure(text=self.filePath)