import cv2

# from vector import Vector


class Particle:
    """The Particle is by default a Circle
    With default thickness or Radius = 20
    """

    def __init__(self, count = 1 ,thickness = 5, color = (255, 255, 255)): 
        """ 
        xv: X Velocity
        yv: Y Valocity

        """
        self.thickness = thickness
        self.color = color
        self.count = count
        if count > 1:
            self = self.return_array_of_particle(count)
            
    def return_array_of_particle(self, count):
            
            return [self for _ in range(count)]
    
    def check_edge(self):
        if self.center[0] > self.img.shape[0]:
            self.center[0] = 0 
        elif self.center[0] < 0:
            self.center[0] = self.img.shape[0] 
        if self.center[1] > self.img.shape[1]:
            self.center[1] = 0
        elif self.center[1] < 0:
            self.center[1] = self.img.shape[1]

    def draw(self):
        cv2.circle(self.img, self.center, self.thickness, self.color, -1)
    
    def __call__(self, img, center):
        self.img = img
        if isinstance(center, tuple):
            self.center = center
        else:
            print("Please pass the center as a tuple!")
        self.draw()

    def __repr__(self):
        return f"{self.count} Particles"