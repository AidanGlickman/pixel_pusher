import requests
from PIL import Image
import time
import random


def rgb_to_hex(r, g, b):
    return ('#{:02X}{:02X}{:02X}').format(r, g, b)

def postImg():
    img = Image.open("cutflag.png")
    for x in range(img.width):
        for y in range(img.height):
            pixel = img.getpixel((x,y))
            if pixel[3] > 100:
                hexed = rgb_to_hex(pixel[0], pixel[1], pixel[2])
                requests.post("http://pixel.acm.illinois.edu/", data=dict(x=x, y=y, color=hexed))

def colorScale():
    for x in range(128):
        for y in range(128):
            hexed = rgb_to_hex(random.randint(0, x+y), random.randint(0, x+y), random.randint(0, x+y))
            print(f"({x}, {y}): {hexed}")
            requests.post("http://pixel.acm.illinois.edu/", data=dict(x=x, y=y, color=hexed))

postImg()