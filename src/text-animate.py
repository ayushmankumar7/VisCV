import numpy as np 
import cv2 

from vector import Vector

from utils.mouse import print_coord
from utils import globals
from units.point import Point
from units.line import Line

from utils.linear_intrep import lerp 

from units.text import Text

globals.initialize_global_variables()
width = 1000
height = 600


p0 = Vector(0, width//2)
p1 = Vector(height // 2, 0)
p2 = Vector(width, height//2)

# while True:
#     p1.x = globals.mouseX
#     p1.y = globals.mouseY
#     a = np.zeros((width, height, 3))   
#     for i in np.linspace(0, 1, 30):
#         x1 = lerp(p0.x, p1.x, i)
#         y1 = lerp(p0.y, p1.y, i)
#         x2 = lerp(p1.x, p2.x, i)
#         y2 = lerp(p1.y, p2.y, i)
#         x = lerp(x1, x2, i)
#         y = lerp(y1, y2, i)
#         # Point(a, int(x), int(y), 2)
#         Line(a, int(x1), int(y1), int(x2), int(y2), 2)
#     cv2.imshow("Plot", a)
#     cv2.setMouseCallback('Plot',print_coord)
#     if cv2.waitKey(10) == 27:
#         break

# cv2.destroyAllWindows()

text = "Hello World"
a = np.zeros((height, width, 3))
font                   = cv2.FONT_HERSHEY_SIMPLEX
fontScale              = 5
fontColor              = (255,255,255)
thickness              = 10
lineType               = 2

t = Text(text, 0, 100, font, fontScale, fontColor, thickness, lineType)

points = t.getTextPoints(sparse = 7)
for i in points:
    Point(a, i[0], i[1], 1)
# a = cv2.add(a, text)

# cv2.imshow("Plot", a)

cv2.imshow("Plot", a)
cv2.waitKey(0)

cv2.destroyAllWindows()