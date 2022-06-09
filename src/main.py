import numpy as np 
import cv2 

from visualization.histogram import Histogram


initialised = False

while True:
    a = np.zeros((600, 600, 3))
    n1 = np.random.randint(1, 400)
    n2 = np.random.randint(1, 400)
    if not initialised:
        r = Histogram(a, [1, 1, 1, 1, 2, 2, 2, 3,3,3,3, 3, 3, 3, 7, 7, 9, 9,9, 9, 5, 5, 10, 10, 10, 10])
        initialised = True
    r(a)
    cv2.imshow("Plot", a)
    if cv2.waitKey(10) == 27:
        break

cv2.destroyAllWindows()
