#!/usr/bin/env python
# https://stackoverflow.com/questions/12062920/how-do-i-create-an-image-in-pil-using-a-list-of-rgb-tuples
# https://stackoverflow.com/questions/40229630/scipy-misc-imshow-runtimeerrorcould-not-execute-image-view

import scipy.misc
import numpy as np
import matplotlib.pyplot as plt

# Image size
width = 640
height = 480
channels = 3

# Create an empty image
img = np.zeros((height, width, channels), dtype=np.uint8)

# Draw something (http://stackoverflow.com/a/10032271/562769)
xx, yy = np.mgrid[:height, :width]
circle = (xx - 100) ** 2 + (yy - 100) ** 2

# Set the RGB values
for y in range(img.shape[0]):
    for x in range(img.shape[1]):
        r, g, b = circle[y][x], circle[y][x], circle[y][x]
        img[y][x][0] = r
        img[y][x][1] = g
        img[y][x][2] = b

# Display the image
#scipy.misc.imshow(img)
plt.imshow(np.uint8(img))
plt.show()

# Save the image
#scipy.misc.imsave("image.png", img)