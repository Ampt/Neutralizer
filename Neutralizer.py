from PIL import Image
import PIL
import time
import numpy as np
import argparse
import cv2
import winsound, sys

from desktopmagic.screengrab_win32 import (
    getDisplayRects, saveScreenToBmp, saveRectToBmp, getScreenAsImage,
    getRectAsImage, getDisplaysAsImages)

lower = [0, 65, 185]
upper = [20, 100, 215]

if __name__ == "__main__":

    while(True):
        im = getScreenAsImage()
        im = im.crop((87, 66, 269, 970))
        b, g, r = im.split()
        im = Image.merge("RGB", (r, g, b))
        image = np.array(im)

        lower = np.array(lower, dtype="uint8")
        upper = np.array(upper, dtype="uint8")

        # find the colors within the specified boundaries and apply
        # the mask
        mask = cv2.inRange(image, lower, upper)
        output = cv2.bitwise_and(image, image, mask=mask)

        if sum(sum(sum(output))) > 0:
            winsound.PlaySound('SONAR.WAV', winsound.SND_FILENAME)
        time.sleep(.5)






# bbox=(110, 80, 307, 954)