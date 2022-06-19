import cv2 

class Line:
    def __init__(self,img, x1, y1, x2, y2, thickness=2, color=(255, 255, 255)):
        self.img = img
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.thickness = thickness
        self.color = color
        self.draw()

    def __str__(self):
        return "({}, {})".format(self.x, self.y)
    
    def __repr__(self) -> str:
        return "({}, {})".format(self.x, self.y)
    
    def draw(self):
        cv2.line(self.img, (int(self.x1), int(self.y1)), (int(self.x2), int(self.y2)), self.color, self.thickness)