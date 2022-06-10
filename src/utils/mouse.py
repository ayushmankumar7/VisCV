import cv2
from utils import globals

def print_coord(event,x,y,flags,param):
    if event == cv2.EVENT_MOUSEMOVE:
        print(f'{x, y}\r', end="")
        globals.mouseX = x
        globals.mouseY = y
