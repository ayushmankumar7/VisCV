import numpy as np 
import cv2 

class Particle:
    def __init__(self, img, thickness = 20):
        self.img = img 
        self.thickness = thickness

    def draw(self):
        cv2.circle(self.img, self.center, self.thickness, (255, 0, 0), -1)
    
    def __call__(self, center):
        if isinstance(center, tuple):
            self.center = center
        else:
            print("Please pass the center as a tuple!")
        self.draw()

while True:
    a = np.zeros((600, 600, 3))
    n1 = np.random.randint(1, 400)
    n2 = np.random.randint(1, 400)
    #a = cv2.circle(a, (n1, n2), 20, (255, 0, 0), -1)
    p = Particle(a)
    p((n1, n2))
    cv2.imshow("Plot", a)
    if cv2.waitKey(10) == 27:
        break

cv2.destroyAllWindows()
