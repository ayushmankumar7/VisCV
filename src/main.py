import numpy as np 
import cv2 

from simulation.particle import Particle

from vector import Vector

initialised = False


state = [1]
width = 600
height = 600

loc = Vector(100, 100)
vel = Vector(1, 3)

while True:
    if len(state) > 0:
        a = np.zeros((width, height, 3))   
        loc = loc + vel
   
        if (loc.x > width) or (loc.x < 0):
            vel.x *= -1 
        if (loc.y > height) or (loc.y < 0):
            vel.y *= -1

        
        
        if not initialised:
            p = Particle()
            initialised = True
        p(a, (loc.x, loc.y))
        
        cv2.imshow("Plot", a)
        if cv2.waitKey(10) == 27:
            break

cv2.destroyAllWindows()
