import cv2

class Particle:
    """The Particle is by default a Circle
    With default thickness or Radius = 20
    """

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
