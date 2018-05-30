import os.path
from PIL import Image

# PATHS
PATH_LOGO = "logo"
PATH_UNDONE = "undone"
PATH_DONE = "done"
# LOGO
NAME_LOGO = "logo.png"
SIZE_LOGO = (1200, 800)
# MAGIC NUMBERS
PADDING = 150

# FUNCTIONS


def isExisted(path, fileName):
    while os.path.isfile(os.path.join(path, fileName)) is False:
        print("Cannot find", fileName + '!')
        input("Press Enter to continue...")
    '''
    Input: Path, Filename
    Output: Return not found file doesn't exist in directory
    '''


def pathJoin(path1, path2):
    return os.path.join(path1, path2)


# Check directories
if not os.path.isdir(PATH_LOGO):
    os.mkdir(PATH_LOGO)
if not os.path.isdir(PATH_UNDONE):
    os.mkdir(PATH_UNDONE)
if not os.path.isdir(PATH_DONE):
    os.mkdir(PATH_DONE)

# Check logo's existence
isExisted(PATH_LOGO, NAME_LOGO)

# Open & Resize logo
logoImg = Image.open(pathJoin(PATH_LOGO, NAME_LOGO))
logoImg = logoImg.resize(SIZE_LOGO)
logoWidth, logoHeight = logoImg.size

# Get number of files
numberOfFiles = len(os.listdir(PATH_UNDONE))

# Set number of done files
numberofDoneFiles = 0

# Status
print('=' * 40 + "\nIMAGE PROTECTION by THANG NGUYEN\n" + '=' * 40)

# Iteration
for fileName in os.listdir(PATH_UNDONE):
    # Open image
    Img = Image.open(pathJoin(PATH_UNDONE, fileName))
    imgWidth, imgHeight = Img.size

    # Add logo
    Img.paste(logoImg, (imgWidth - logoWidth - PADDING,
                        imgHeight - logoHeight - PADDING), logoImg)

    # Save change
    Img.save(pathJoin(PATH_DONE, fileName))

    # Remove old file
    os.remove(pathJoin(PATH_UNDONE, fileName))

    # Count done file
    numberofDoneFiles += 1

    # Status
    print('\r\n' + str(numberofDoneFiles) + '/' + str(numberOfFiles) + ' [' +
          str(int(numberofDoneFiles/numberOfFiles*100)) + '%] - '
          + fileName, end='')
