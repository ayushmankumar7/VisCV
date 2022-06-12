import numpy as np
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y 

    def mag(self):
        """
            Return the magnitude of a Vector
        """
        return np.sqrt((self.x**2) + (self.y**2))

    def normalize(self):
        return self / self.mag()

    def limit(self, x):
        if self.mag()> x:
            return (self.normalize()) * x
        else:
            return self

    def random2D(self):
        self.x = np.random.randn()
        self.y = np.random.randn()
        return self.normalize()
    
    def __add__(self, vector):
        """ 
        v = v1 + v2
        v_x = v1_x + v2_x
        v_y = v1_y + v2_y
        return v
        """

        if isinstance(vector, type(self)):
            return Vector(*(x + y for x, y in zip((self.x, self.y), (vector.x, vector.y))))
        else:
            return "Please add a Vector!"
    
    def __sub__(self, vector):
        """ 
        
        v = v1 - v2
        v_x = v1_x - v2_x
        v_y = v1_y - v2_y

        return v
        """

        if isinstance(vector, type(self)):
            return Vector(*(x - y for x, y in zip((self.x, self.y), (vector.x, vector.y))))
        else:
            return "Please substract a Vector!"


    def __mul__(self, scalar):
        """ 
        v_x = v1_x * scalar
        v_y = v1_y + scalar

        return v
        """

        if isinstance(scalar, type(self)):
            return "Please multiply a non Vector"
        else:
            return Vector(self.x*scalar, self.y*scalar)

    def __truediv__(self, scalar):
        if isinstance(scalar, type(self)):
            return "Please Divide by a Scalar"
        else:
            if scalar != 0:
                return Vector(self.x/scalar, self.y/scalar)
            else:
                return "ERROR! Division by 0 not possible!!" 

    def __repr__(self):
        return f"Vector at: ({self.x}, {self.y})"

if __name__ == "__main__":
    loc = Vector(9, 8)
    vel = Vector(1, 3)
    # print(vel)
    # print(loc)
    # print(vel + loc)
    print(loc.normalize())
    # print(Vector.random2D())