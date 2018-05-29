#! python3

# Load the logo image.
# Loop over all .png and.jpg files in the working directory.
# Paste the logo image into the corner.
# Save the altered images to another folder.

# This means the code will need to do the following:
# Open the catlogo.png file as an Image object.
# Loop over the strings returned from os.listdir('.') .
# Call the paste() method to paste the logo.
# Call the save() method to save the changes, using the original filename.

import os.path

from PIL import Image

PATH_LOGO = './logo/'
PATH_UNDONE = './undone/'
PATH_DONE = './done/'
PADDING = 50

# Check directories
if not os.path.isdir(PATH_LOGO):
    os.mkdir(PATH_LOGO)
if not os.path.isdir(PATH_UNDONE):
    os.mkdir(PATH_DONE)
if not os.path.isdir(PATH_DONE):
    os.mkdir(PATH_DONE)

# Check logo
while os.path.isfile(PATH_LOGO + "logo.png") is not True:
    print("There is no logo!")

# Open logo
logoImg = Image.open(PATH_LOGO + "logo.png")

# Get Number of files
numberOfFiles = len(os.listdir(PATH_UNDONE))

numberofDoneFiles = 0

for fileName in os.listdir(PATH_UNDONE):
    # Open image
    Img = Image.open(PATH_UNDONE + fileName)
    imgWidth, imgHeight = Img.size

    # Resize logo
    logoImg = logoImg.resize((1200, 800))
    logoWidth, logoHeight = logoImg.size

    # Add logo
    Img.paste(logoImg, (imgWidth - logoWidth - PADDING,
              imgHeight - logoHeight - PADDING), logoImg)
    # Save change
    Img.save(os.path.join(PATH_DONE, fileName))
    # Delete original
    os.remove(PATH_UNDONE + fileName)

    numberofDoneFiles += 1

    # Progress
    print('\r' + str(numberofDoneFiles) + '/' + str(numberOfFiles) + ' [' +
          str(numberofDoneFiles/numberOfFiles*100) + '%] - '
          + fileName, end='')
# DONE
print("\nDone!")
