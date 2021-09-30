import requests
from PIL import Image
import time
import random
import sys
import argparse
import numpy as np

class ImageClass:
    IMG_HEIGHT = 128
    IMG_WIDTH = 128

    @staticmethod
    def getPixels(imgPath):
        img = Image.open(imgPath).resize((ImageClass.IMG_HEIGHT, ImageClass.IMG_WIDTH))
        return np.array(img)

    def __init__(self, imgPath, transThresh):
        self.imgPath = imgPath
        self.pixels = ImageClass.getPixels(imgPath)
        self.transThresh = transThresh


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


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Interact with ACM Pixel.")
    parser.add_argument("method", metavar="M", action="store", nargs=1, default="image_linear")
