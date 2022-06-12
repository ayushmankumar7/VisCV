import numpy as np 
import cv2 

from vector import Vector

from utils.mouse import print_coord
from utils import globals
from simulation.particle import Particle
from units.point import Point

globals.initialize_global_variables()

initialised = False


state = [1]
width = 600
height = 600



loc = Vector(width // 2, height // 2)
vel = Vector(0, 0)

""" 
Add Array of Particles



"""



while True:

    mouse = Vector(globals.mouseX, globals.mouseY)
    dir = mouse - loc    
    acc =dir.normalize()
    
    acc = acc * 0.5
    vel += acc 
    vel = vel.limit(5)
    loc += vel 
    
    a = np.zeros((width, height, 3))   
    for i in range(5):
        Point(a, int(loc.x), int(loc.y))

    cv2.imshow("Plot", a)
    cv2.setMouseCallback('Plot',print_coord)
    if cv2.waitKey(10) == 27:
        break

cv2.destroyAllWindows()
