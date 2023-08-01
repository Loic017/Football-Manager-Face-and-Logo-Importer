# Football Manager Face and Logo Importer ⚽
A program to import player faces or team logos individually into Football Manager.

Have a newgen you want to give a specific face? Maybe you want to give an existing legend a special picture with a trophy. Have a custom logo you made for your team? This program allows you to easily import them into the game individually, avoiding the hassle of resizing images, renaming them and the rest of the mess.

This program auto resizes imported images into the correct sizes, creating two versions for the icon and larger variants of FM images. Alongside this, an XML config file is automatically generated.

***

# How to use
## Prerequisites
### Getting IDs

1. To get the ID of a team or player, go to the ingame settings -> advanced -> interface -> skin and toggle on "Show screen IDs..."

<img width="254" alt="image" src="https://github.com/Loic017/Football-Manager-Face-and-Logo-Importer/assets/105462797/5b07e40f-2e01-48a3-9c97-5c71d94fd7e1">

2. The id will show up on the search bar (Unfortunately you cant copy and paste it) 

<img width="331" alt="image" src="https://github.com/Loic017/Football-Manager-Face-and-Logo-Importer/assets/105462797/06f7e196-49d4-4d4a-bb10-f7ea987f50b6">

### Graphics Folder

1. By default, FM wont come with a graphics folder, so the user must create one

2. Find the Football Manager folder for your version (e.g. Football Manager 2023 folder). It is usually found within the Sports Interactive folder (...\Documents\Sports Interactive\Football Manager 2023)

3. Within the Football Manager 20XX folder, create a folder called "graphics"

<img width="271" alt="image" src="https://github.com/Loic017/Football-Manager-Face-and-Logo-Importer/assets/105462797/94876ee6-d9bd-4205-9673-b57c07f2cc7b">

4. Go into the graphics folder and copy the directory (...Documents\Sports Interactive\Football Manager 2023\graphics)

## Using the Program

1. Open the program

<img width="487" alt="image" src="https://github.com/Loic017/Football-Manager-Face-and-Logo-Importer/assets/105462797/5d82f86e-cae4-409f-a33f-cd9e5e2aa1ef">

2. Browse and select the graphics folder (paste the directory that was copied into the file explorer to find it quicker)

3. Select if you are importing a team logo or a player image

4. Browse and select the image file you want to import

5. Enter the ID (the one found in the search bar) into the text input box

6. Press the import button

7. Finished! Your image is automatically resized and a config file is automatically generated. Happy FMing!

***

# Demo

- Timo Werner doesnt have a face, his ID is 92051583
<img width="300" alt="image" src="https://github.com/Loic017/Football-Manager-Face-and-Logo-Importer/assets/105462797/b061e898-b68a-4dd3-ac26-1239c6313442">

- I will change it to this picture of him
<img width="150" alt="image" src="https://github.com/Loic017/Football-Manager-Face-and-Logo-Importer/assets/105462797/e510b2ef-bd77-43ba-888e-4f07d6653a38">

- I then input the correct entries into the program and press Import
<img width="347" alt="image" src="https://github.com/Loic017/Football-Manager-Face-and-Logo-Importer/assets/105462797/fc51c04b-ac87-4612-bd5c-3a8f37474474">

- Boom, he now has a face in the game!
<img width="300" alt="image" src="https://github.com/Loic017/Football-Manager-Face-and-Logo-Importer/assets/105462797/7c52962e-b182-417f-9a90-375e369281e5">


***

# Technical Information
A python GUI application build with customtkinterincluding Pilow for image handling and ElementTree XML for generating the XML config files.

## Libraries Used
See ![requirements.txt](https://github.com/Loic017/Football-Manager-Face-and-Logo-Importer/blob/main/requirements.txt)

Customtkinter:
[Website](https://customtkinter.tomschimansky.com/)

Pyinstaller is used to create the .exe

***

# Future Improvements
- Improved resizing: Aspect ratio and other methods to keep the image from stretching too much
- Competition image importing
- ~~Save graphics folder: No need to choose the graphics folder on each boot up~~ ✅
- Fix bug where you cannot import an image right after importing one (User has to restart program after every use)
