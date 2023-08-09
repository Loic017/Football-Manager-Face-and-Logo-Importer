import customtkinter as ct
from PIL import Image
from importComponents import GraphicsFolderFrame, ImportTypeFrame, UploadImageFrame
import os
from generateConfig import generateConfig
from saveGraphicsPath import saveGraphicsPath, loadGraphicsPath


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

        saveGraphicsPath(self.graphicsPath)

        image = Image.open(str(self.imagePath))
        # Resize images to correct Football Manager dimensions
        if self.importType == "logo":
            # Calculate dimensions
            normal_width = 200
            normal_height = 200
            small_width = 20
            small_height = 20

            current_width, current_height = image.size

            if current_height > current_width:
                normal_height = int((normal_width / current_width) * current_height)
                small_height = int((small_width / current_width) * current_height)
            else:
                normal_width = int((normal_height / current_height) * current_width)
                small_width = int((small_height / current_height) * current_width)
            normalLogo = image.resize((normal_width, normal_height))
            smallLogo = image.resize((small_width, small_height))

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
            generateConfig(self.fmId, True, parentDir, "normal/", "small/")

        elif self.importType == "player":
            # Calculate dimensions
            normal_width = 250
            normal_height = 250
            small_width = 20
            small_height = 20

            current_width, current_height = image.size

            if current_height > current_width:
                normal_height = int((normal_width / current_width) * current_height)
                small_height = int((small_width / current_width) * current_height)
            else:
                normal_width = int((normal_height / current_height) * current_width)
                small_width = int((small_height / current_height) * current_width)
            portraitFace = image.resize((normal_width, normal_height))
            iconFace = image.resize((small_width, small_height))

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
            generateConfig(self.fmId, False, parentDir, "portrait/", "icon/")

# Main App
class App(ct.CTk):
    def __init__(self):
        super().__init__()
        ct.set_appearance_mode("dark")
        ct.set_default_color_theme("blue")

        # Graphics Folder Frame
        self.graphicsFolder = GraphicsFolderFrame(self)
        self.graphicsFolder.grid(row=0, column=0, padx=20, pady=(20, 0), sticky="nsew")

        # Select Import Type
        self.importTypeFr = ImportTypeFrame(self)
        self.importTypeFr.grid(row=1, column=0, padx=20, pady=(20, 0), sticky="nsew")

        # Import Image Frame
        self.uploadImage = UploadImageFrame(self)
        self.uploadImage.grid(row=1, column=1, padx=20, pady=(20, 0), sticky="nsew")

        # Finish Import
        self.finishImport = FinishImportFrame(
            self, self.graphicsFolder, self.importTypeFr, self.uploadImage
        )
        self.finishImport.grid(row=2, column=0, padx=20, pady=(20, 0), sticky="nsew")

        # app = ct.CTk()
        self.geometry("800x900")
        self.title("Football Manager Importer")


# Run App
app = App()
app.mainloop()
