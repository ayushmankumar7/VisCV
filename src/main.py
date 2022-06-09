import numpy as np 
import cv2 

class Particle:
    """The Particle is by default a Circle
    With default thickness or Radius = 20
    """

    def __init__(self, img, thickness = 20):
        self.img = img 
        self.thickness = thickness
        self.near = 1
        self.far = self.near + 2

    def draw(self):
        cv2.circle(self.img, self.center, self.thickness, (255, 0, 0), -1)
    
    def __call__(self, center):
        if isinstance(center, tuple):
            self.center = center
        else:
            print("Please pass the center as a tuple!")
        self.draw()

class Histogram:
    def __init__(self,img, arr):
        self.img = img
        self.arr = arr
        self.color_register = {}

    def get_coords(self, t):
        """ 
        Argument [ t ]:
        Naming convention: 
        'c'     - Center
        'l'     - Left 
        'r'     - Right

        if l2 - This means 2 places relative to center 
        """
        w, h, _ = self.img.shape
        self.p = w // len(self.find_freq())
        center = (len(self.find_freq()) // 2 ) 
        if t == 'c' and len(t) == 1:
            y0 = h
            x0 = (w // 2) - (self.p // 2)
            x1 = (w // 2) + (self.p // 2)
            y1 = h//2
        else:
            if t[0] == 'l':
                y0 = h
                y1 = h // self.find_freq()[center - int(t[1:])]
                x0 = (w // 2) - ((self.p // 2) *(int(t[1:])+(int(t[1:]) - 1) + 2))
                x1 = (w // 2) - ((self.p // 2) * (int(t[1:])+(int(t[1:]) - 1)))
                
            if t[0] == 'r':
                y0 = h
                y1 = h // self.find_freq()[center + int(t[1:])]
                x0 = (w // 2) + ((self.p // 2) *(int(t[1:])+(int(t[1:]) - 1) + 2))
                x1 = (w // 2) + ((self.p // 2) *(int(t[1:])+(int(t[1:]) - 1)))

        return (x0, y0), (x1, y1)

    def draw(self, n1, n2):
        colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (100, 255,255), (40, 255, 255), (200, 75, 65), (20, 56, 90), (50, 50, 30), (90, 150, 150)]
        color = colors[np.random.randint(0, len(colors) - 1)]
        if str(n1)+str(n2) in self.color_register:
            cv2.rectangle(self.img, n1, n2, (int(self.color_register[str(n1)+str(n2)][0]), int(self.color_register[str(n1)+str(n2)][1]), int(self.color_register[str(n1)+str(n2)][2])) , -1)
            
        else:
            self.color_register[str(n1)+str(n2)] = color


    def __call__(self, img):
        self.img = img
        self.calc_hist()
    
    def calc_hist(self):
        if self.is_odd():
            center = (len(self.find_freq()) // 2 )
            for i in range(len(self.find_freq())):
                if i == center:
                    n1, n2 = self.get_coords('c')
                else:
                    r = i - center
                    if r < 0:
                        n1, n2 = self.get_coords(f'l{abs(r)}')
                    else:
                        n1, n2 = self.get_coords(f'r{abs(r)}')
                self.draw(n1, n2)
        else:
            pass 

    def is_odd(self):
        if len(self.find_freq()) % 2 == 0:
            return False
        else:
            return True

    def find_freq(self):
        d= {}
        for i in self.arr:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        return list(d.values())


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
