import cv2

from vector import Vector


class Particle(Vector):
    """The Particle is by default a Circle
    With default thickness or Radius = 20
    """

    def __init__(self,xv = 0, yv = 0, thickness = 20, color = (255, 255, 255)): 
        """ 
        xv: X Velocity
        yv: Y Valocity

        """
        super(Particle, self).__init__( xv,yv )
        self.thickness = thickness
        self.color = color
        self.xv = xv
        self.yv = yv

    def draw(self):
        cv2.circle(self.img, self.center, self.thickness, self.color, -1)
    
    def __call__(self, img, center):
        self.img = img
        if isinstance(center, tuple):
            self.center = center
        else:
            print("Please pass the center as a tuple!")
        self.draw()
