import cv2
from PIL import Image, ImageStat
import numpy
import screen_brightness_control as sbc
from numpy import interp

vc = cv2.VideoCapture(0)

if vc.isOpened():
    rval, frame = vc.read()
else:
    rval = False

def brightness(frame):
    return numpy.mean(frame)

while rval:
    rval, frame = vc.read()
    key = cv2.waitKey(20)
    bright = brightness(frame)
    sbc.set_brightness(int(interp(bright, [1, 255], [0, 100])))
