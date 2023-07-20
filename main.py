import customtkinter as ct
from PIL import Image
from importComponents import GraphicsFolderFrame, ImportTypeFrame, UploadImageFrame
import os
from generateConfig import generateConfig


# Finish Import Frame
class FinishImportFrame(ct.CTkFrame):
    def __init__(self, master, graphicsFolder, importType, filePath):
        super().__init__(master)
        # Other Frames - Type Class
        self.graphicsFolder = graphicsFolder
        self.importType = importType
        self.filePath = filePath

        self.finishStepLabel = ct.CTkLabel(self, text="STEP 4")
        self.finishStepLabel.pack(padx=0, pady=5)

        # User input ID
        self.idLabel = ct.CTkLabel(
            self, text="Enter Football Manager ID", fg_color="gray30", corner_radius=6
        )
        self.idLabel.pack(padx=0, pady=5)
        self.idInput = ct.CTkEntry(self)
        self.idInput.pack(padx=20, pady=3)

        # Button to activate processImport function
        self.finishButton = ct.CTkButton(
            self, text="Import", command=self.processImport
        )
        self.finishButton.pack(padx=20, pady=20)

    # Process user inputs to import selected images
    def processImport(self):
        self.graphicsPath = self.graphicsFolder.filePathPath.cget("text")
        self.importType = self.importType.importTypeVar.get()
        self.imagePath = self.filePath.imagePathLabel.cget("text")
        self.fmId = self.idInput.get()

        image = Image.open(str(self.imagePath))
        # Resize images to correct Football Manager dimensions
        if self.importType == "logo":
            normalLogo = image.resize((200, 200))
            smallLogo = image.resize((20, 20))

            # Create directory if it doesnt exist
            normalDir = "{}/{}/teamLogo/normal/".format(
                str(self.graphicsPath), str(self.fmId)
            )
            smallDir = "{}/{}/teamlogo/small/".format(
                str(self.graphicsPath), str(self.fmId)
            )

            os.makedirs(normalDir, exist_ok=True)
            os.makedirs(smallDir, exist_ok=True)

            # Save Images
            normalLogo.save("{}{}.png".format(normalDir, str(self.fmId)), "PNG")
            smallLogo.save("{}{}.png".format(smallDir, str(self.fmId)), "PNG")

            # Generate config.xml
            parentDir = "{}/{}/teamlogo/config.xml".format(
                str(self.graphicsPath), str(self.fmId)
            )
            generateConfig(self.fmId, True, parentDir, normalDir, smallDir)

        elif self.importType == "player":
            portraitFace = image.resize((200, 200))
            iconFace = image.resize((20, 20))

            # Create directory if it doesnt exist
            normalDir = "{}/{}/playerFaces/portrait/".format(
                str(self.graphicsPath), str(self.fmId)
            )
            iconDir = "{}/{}/playerFaces/icon/".format(
                str(self.graphicsPath), str(self.fmId)
            )

            os.makedirs(normalDir, exist_ok=True)
            os.makedirs(iconDir, exist_ok=True)

            # Save Images
            portraitFace.save("{}{}.png".format(normalDir, str(self.fmId)), "PNG")
            iconFace.save("{}{}.png".format(iconDir, str(self.fmId)), "PNG")

            # Generate config.xml
            parentDir = "{}/{}/playerFaces/config.xml".format(
                str(self.graphicsPath), str(self.fmId)
            )
            generateConfig(self.fmId, False, parentDir, normalDir, iconDir)


# Main App
class App(ct.CTk):
    def __init__(self):
        super().__init__()
        ct.set_appearance_mode("dark")
        ct.set_default_color_theme("blue")

        # Graphics Folder Frame
        self.graphicsFolder = GraphicsFolderFrame(self)
        self.graphicsFolder.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsew")

        # Select Import Type
        self.importType = ImportTypeFrame(self)
        self.importType.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="nsew")

        # Import Image Frame
        self.uploadImage = UploadImageFrame(self)
        self.uploadImage.grid(row=1, column=1, padx=10, pady=(10, 0), sticky="nsew")

        # Finish Import
        self.finishImport = FinishImportFrame(
            self, self.graphicsFolder, self.importType, self.uploadImage
        )
        self.finishImport.grid(row=2, column=0, padx=10, pady=(10, 0), sticky="nsew")

        # app = ct.CTk()
        self.geometry("650x650")
        self.title("Football Manager Importer")


# Run App
app = App()
app.mainloop()
