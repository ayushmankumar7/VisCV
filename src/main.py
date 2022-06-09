import numpy as np 
import cv2 

#from visualization.histogram import Histogram
from simulation.particle import Particle

initialised = False

i = 10
j = 300
s = 0

state = []

while True:
    if len(state) > 0:
        a = np.zeros((600, 600, 3))
        
        a = cv2.addWeighted(a, 1.0, state[-1], 0.5, 0.0)
        if i < 500 and s == 0:
            i += 4
    
        elif i < 10:    
            s = 0
        else:
            s = 1
            if s == 1:
                i -= 4

        if not initialised:
            p = Particle()
            initialised = True
        p(a, (i, j))
        if len(state) > 7:
            state.pop(0)
        state.append(a)
        
        cv2.imshow("Plot", a)
        if cv2.waitKey(10) == 27:
            break
    else:
        state.append(np.zeros((600, 600, 3)))
cv2.destroyAllWindows()
