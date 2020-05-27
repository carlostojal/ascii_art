
import sys
import numpy
import PIL
from PIL import Image, ImageDraw

# chars from the darkest to the lightest
chars = ["\"", "`", "^", "\\", ":", ";", "I", "l", "!", "i", "~", "+", "_", "-", "?", "]", "[", "}", "{", "1", ")", "(", "|", "/", "t", "f", "j", "r", "x", "n", "u", "v", "c", "z", "X", "Y", "U", "J", "C", "L", "Q", "0", "O", "Z", "m", "w", "q", "p", "d", "b", "k", "h", "a", "o", "*", "#", "M", "W", "&", "8", "%", "B", "@", "$"]

maxsize = (150, 150) # downscale to use

success = True

print("Starting...")

try:
    img_path = sys.argv[1] # image path from argument
except IndexError:
    print("Image not given.\n")
    print("Usage: \"python main.py path/to/img\"")
    success = False

if success:
    try:
        img = Image.open(img_path).convert('LA') # open image and convert to black and white
    except PIL.UnidentifiedImageError:
        print("Error reading image. Probably given file is not an image.")
        success = False
    except FileNotFoundError:
        print("Image not found.")
        success = False
    
    if success:
        img.thumbnail(maxsize, Image.ANTIALIAS) # downscale image
        img.show()

        img_array = numpy.asarray(img)

        ascii_art = ""

        print("Converting to ASCII art...")
        for row in img_array:
            for pixel in row:
                correspondent_char = chars[int(pixel[0] / (255 / len(chars))) - 1]
                ascii_art += correspondent_char + " "
            ascii_art += "\n" 

        print("Saving result...")

        img_out = Image.new('RGB', (6 * len(ascii_art.split("\n")[0]), 14 * len(ascii_art.split("\n"))), color = (0, 0, 0))

        d = ImageDraw.Draw(img_out)
        d.text((0, 0), ascii_art, fill = (255, 255, 255))
        img_out.save("../data/out.png")
        img_out.show()

        f = open("../data/out.txt", "w")
        f.write(ascii_art)
        f.close()

        print("Done")
