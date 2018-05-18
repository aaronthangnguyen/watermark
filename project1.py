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


import os
from PIL import Image

LOGO_FILENAME = './logo/logo.png'

logoIm = Image.open(LOGO_FILENAME)
logoWidth, logoHeight = logoIm.size

print((str(logoWidth) + "and" + str(logoHeight)))

# Loop

PATH_UNDONE = './undone/'
PATH_DONE = './done/'

for filename in os.listdir(PATH_UNDONE):
    im = Image.open(PATH_UNDONE + filename)

    imWidth, imHeight = im.size
    print((str(imWidth) + " and " + str(imHeight)))
    print('Adding logo to %s...' %(filename))

    # Paste
    im.paste(logoIm, (imWidth - logoWidth, imHeight - logoHeight), logoIm)

    # Save
    print('Saving to %s...' %(PATH_DONE))
    im.save(os.path.join(PATH_DONE, filename))