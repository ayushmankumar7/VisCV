import numpy as np 
import cv2 

from vector import Vector

from utils.mouse import print_coord

mouseX = 0
mouseY = 0

def print_coord(event,x,y,flags,param):
    global mouseX, mouseY
    if event == cv2.EVENT_MOUSEMOVE:
        print(f'{x, y}\r', end="")
        mouseX = x
        mouseY = y

initialised = False



state = [1]
width = 600
height = 600

center = Vector(width // 2, height // 2)

while True:

    a = np.zeros((width, height, 3))   
    
    mouse = Vector(mouseX, mouseY)
    mouse = mouse

    cv2.line(a, (mouse.x, mouse.y),(center.x, center.y),  (255, 255, 255))
    
    cv2.imshow("Plot", a)
    cv2.setMouseCallback('Plot',print_coord)
    if cv2.waitKey(10) == 27:
        break

cv2.destroyAllWindows()
