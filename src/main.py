
import sys
import numpy
import PIL
from PIL import Image, ImageDraw

# chars from the lightest to the darkest
chars = ["\"", "`", "^", "\\", ":", ";", "I", "l", "!", "i", "~", "+", "_", "-", "?", "]", "[", "}", "{", "1", ")", "(", "|", "/", "t", "f", "j", "r", "x", "n", "u", "v", "c", "z", "X", "Y", "U", "J", "C", "L", "Q", "0", "O", "Z", "m", "w", "q", "p", "d", "b", "k", "h", "a", "o", "*", "#", "M", "W", "&", "8", "%", "B", "@", "$"]

maxsize = (150, 150)

img_path = sys.argv[1]

print("Starting...")

img = Image.open(img_path).convert('LA') # open image and convert to black and white
img.thumbnail(maxsize, Image.ANTIALIAS) # downscale image
img.resize((1920, 700))
img.show()

img_out = Image.new('RGB', (1920, 1080), color = (0, 0, 0))

img_array = numpy.asarray(img)

ascii_art = ""

print("Converting to ASCII art...")
for row in img_array:
    for pixel in row:
        correspondent_char = chars[int(pixel[0] / (255 / len(chars))) - 1]
        ascii_art += correspondent_char + " "
    ascii_art += "\n" 

print("Saving result...")

d = ImageDraw.Draw(img_out)
d.text((0, 0), ascii_art, fill = (255, 255, 255))
img_out.save("../data/out.png")
img_out.show()

f = open("../data/out.txt", "w")
f.write(ascii_art)
f.close()

print("Done")