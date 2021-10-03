#!/usr/bin/env python3
import requests
from PIL import Image
import abc
import argparse
import numpy as np

BASE_URL = "http://pixel.acm.illinois.edu/"
class ImageClass:
    __metaclass__ = abc.ABCMeta
    IMG_HEIGHT = 128
    IMG_WIDTH = 128

    @staticmethod
    def getPixels(imgPath):
        """
        Returns a numpy array representing the pixels of the image, reshaped to the size of pixel.
        @TODO implement alternative resize methods
        """
        img = Image.open(imgPath).resize((ImageClass.IMG_HEIGHT, ImageClass.IMG_WIDTH))
        return np.array(img)
    
    @staticmethod
    def toHex(pixel):
        return ('#{:02X}{:02X}{:02X}').format(pixel[0], pixel[1], pixel[2])

    def __init__(self, imgPath, transThresh, dry):
        self.imgPath = imgPath
        self.pixels = ImageClass.getPixels(imgPath)
        self.transThresh = transThresh
        self.dry = dry

    @abc.abstractmethod
    def draw(self):
        """
        Send POST requests to actually draw the image to pixel.
        """
        return

class LinearImage(ImageClass):
    def __init__(self, imgPath, transThresh=100, dry=False):
        super().__init__(imgPath, transThresh, dry)
    
    def draw(self):
        for y, row in enumerate(self.pixels):
            for x, pixel in enumerate(row):
                if(pixel[3] > self.transThresh):
                    pixelStr = ImageClass.toHex(pixel)
                    requests.post(BASE_URL,  data=dict(x=x, y=y, color=pixelStr))


TYPE_NAMES = {"image_linear": LinearImage}

def drawDriver(args):
    imageDriver = TYPE_NAMES[args.method[0]](args.file[0])
    imageDriver.draw()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Interact with ACM Pixel.")
    
    parser.add_argument("--file", "-F", dest="file", metavar="FileName", action="store", nargs=1)
    parser.add_argument("--method", "-M", dest="method", metavar="Method", action="store", nargs=1, default="image_linear")
    
    args = parser.parse_args()
    drawDriver(args)

