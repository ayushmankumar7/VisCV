class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y 
    
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


    def __mult__(self, scalar):
        """ 
        v_x = v1_x * scalar
        v_y = v1_y + scalar

        return v
        """

        if isinstance(vector, type(self)):
            return "Please multiply a non Vector"
        else:
            return Vector(self.x/scalar, self.y/scalar)

    def __repr__(self):
        return f"Vector at: ({self.x}, {self.y})"

if __name__ == "__main__":
    loc = Vector(9, 0)
    vel = Vector(1, 3)
    print(vel)
    print(loc)
    print(vel + loc)
