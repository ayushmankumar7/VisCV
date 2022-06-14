import cv2 
import numpy as np

class Text:
    def __init__(self, text, x, y, font, font_scale = 5, font_color = (255, 255 ,255), thickness = 10, line_type = 2):
        self.text = text
        self.x = x
        self.y = y
        self.font = font
        self.font_scale = font_scale
        self.font_color = font_color
        self.thickness = thickness
        self.line_type = line_type

    def drawText(self): 
        screen = np.zeros(self.getScreenDimensions())
        cv2.putText(screen, self.text, 
            (0, 200), 
            self.font, 
            self.font_scale,
            self.font_color,
            self.thickness,
            self.line_type)
        return screen 

    def draw(self, a):
        h, w, _ = self.getScreenDimensions()
        if self.y + w > a.shape[1]:
            print("ERROR")
            return "Error: Screen not big enough to Display Text"
        a[self.x: self.x + h, self.y: self.y + w, :] = self.drawText()
        return a

    def getTextPoints(self, sparse = 0):
        xy_coords = np.flip(np.column_stack(np.where(self.getEdgeImage() > 0)), axis=1)
        if sparse > 0:
            return xy_coords[::sparse]
        return xy_coords

    def getEdgeImage(self):
        edge = cv2.Canny(np.uint8(self.drawText()), 100, 200)
        return edge

    def getTextLength(self):
        return len(self.text)
    
    def getScreenDimensions(self):
        return (300, self.getTextLength() * 81, 3)

