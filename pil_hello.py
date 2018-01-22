# http://effbot.org/imagingbook/introduction.htm
# https://en.wikibooks.org/wiki/Python_Imaging_Library/Editing_Pixels
# http://pillow.readthedocs.io/en/3.1.x/reference/ImageDraw.html

import PIL.ImageDraw as ImageDraw
import PIL.Image as Image
import random as rnd

inputFilePath = "input.jpg"
outputFilePath = "output.png"

image = Image.open(inputFilePath) #Image.new("RGB", (640, 480))
draw = ImageDraw.Draw(image)
print (str(image.format) + " " + str(image.size) + " " + str(image.mode))

box = (100,100,400,400)
region = image.crop(box)
region = region.transpose(Image.ROTATE_180)
image.paste(region, box)

pixels = image.load()
for i in range(image.size[0]):
    for j in range(image.size[1]):
        c = list(pixels[i,j])
        c[0] += i
        c[1] += j
        c[2] += 0 
        pixels[i,j] = tuple(c)

points = []
for i in range(0, 100):
    points.append((rnd.randrange(image.size[0]), rnd.randrange(image.size[1])))
draw.polygon(points, fill=(127, 127, 127), outline=(255,255,255))

image.save(outputFilePath)