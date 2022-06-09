import cv2

class Particle:
    """The Particle is by default a Circle
    With default thickness or Radius = 20
    """

    def __init__(self,thickness = 20, color = (255, 255, 255)): 
        self.thickness = thickness
        self.color = color
        
    def draw(self):
        cv2.circle(self.img, self.center, self.thickness, self.color, -1)
    
    def __call__(self, img, center):
        self.img = img
        if isinstance(center, tuple):
            self.center = center
        else:
            print("Please pass the center as a tuple!")
        self.draw()
