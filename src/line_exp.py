import numpy as np 
import cv2 

from vector import Vector

from utils.mouse import print_coord
from utils import globals
from visualization.trackbar import TrackBar


globals.initialize_global_variables()

initialised = False


state = [1]
width = 600
height = 600

center = Vector(width // 2, height // 2)

while True:
    if not initialised:
        t = TrackBar()
        initialised = True

    a = np.zeros((width, height, 3))   
    
    mouse = Vector(globals.mouseX, globals.mouseY)
    t(a, int(abs(mouse.x - center.x) / (width//2) * 100))
    cv2.line(a, (mouse.x, mouse.y),(center.x, center.y),  (255, 255, 255))

    cv2.imshow("Plot", a)
    cv2.setMouseCallback('Plot',print_coord)
    if cv2.waitKey(10) == 27:
        break

cv2.destroyAllWindows()
