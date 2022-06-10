import cv2

def print_coord(event,x,y,flags,param):
    if event == cv2.EVENT_MOUSEMOVE:
        print(f'{x, y}\r', end="")
