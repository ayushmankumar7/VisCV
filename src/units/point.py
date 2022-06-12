import cv2 

class Point:
    def __init__(self,img, x, y, thickness=5, color=(255, 255, 255)):
        self.img = img
        self.x = x
        self.y = y
        self.thickness = thickness
        self.color = color
        self.draw()

    def __str__(self):
        return "({}, {})".format(self.x, self.y)
    
    def __repr__(self) -> str:
        return "({}, {})".format(self.x, self.y)
    
    def draw(self):
        cv2.circle(self.img, (self.x, self.y), 5, self.color, -1)