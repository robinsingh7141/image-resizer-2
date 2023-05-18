#image_resizer2

import cv2

# Ask user for source image, destination and dimensions
source = input("Enter the path of the source image: ")
destination = input("Enter the path of the destination image: ")
new_width = int(input("Enter new width for the image: "))
new_height = int(input("Enter new height for the image: "))

# read the image
src = cv2.imread(source, cv2.IMREAD_UNCHANGED)

# resize the image
output = cv2.resize(src, (new_width, new_height))

cv2.imwrite(destination, output)
