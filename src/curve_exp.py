import numpy as np 
import cv2 

from vector import Vector

from utils.mouse import print_coord
from utils import globals
from units.point import Point
from utils.linear_intrep import lerp 


globals.initialize_global_variables()

width = 600
height = 600


p0 = Vector(0, 300)
p1 = Vector(300, 0)
p2 = Vector(600, 300)

while True:
    p1.x = globals.mouseX
    p1.y = globals.mouseY
    a = np.zeros((width, height, 3))   
    for i in np.linspace(0, 1, 10):
        x1 = lerp(p0.x, p1.x, i)
        y1 = lerp(p0.y, p1.y, i)
        x2 = lerp(p1.x, p2.x, i)
        y2 = lerp(p1.y, p2.y, i)
        x = lerp(x1, x2, i)
        y = lerp(y1, y2, i)
        Point(a, int(x), int(y), 2)

    cv2.imshow("Plot", a)
    cv2.setMouseCallback('Plot',print_coord)
    if cv2.waitKey(10) == 27:
        break

cv2.destroyAllWindows()
