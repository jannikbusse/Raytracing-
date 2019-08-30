import numpy as np

class Vector(object):
    x = 0
    y = 0
    z = 0

    def __init__(self, x = 0, y = 0, z = 0):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return "("+str(self.x) + ", " + str(self.y) + ", " + str(self.z)+")"


    def set(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def len(self):
        return np.sqrt(self.x*self.x + self.y*self.y + self.z*self.z)

    def add(self, v2):        
        return Vector(self.x + v2.x, self.y + v2.y, self.z + v2.z)


    def sub(self, v2):
        return Vector(self.x - v2.x, self.y - v2.y, self.z - v2.z)

    def dst(self, v2):
        b1 = v2.x
        b2 = v2.y
        b3 = v2.z
        return np.sqrt((b1 - self.x)*(b1 - self.x)+(b2 - self.y)*(b2 - self.y)+(b3 - self.z)*(b3 - self.z))

    def scale(self, s):
        return Vector(self.x *s, self.y * s, self.z *s)

    def norm(self):
        return self.scale(1/self.len)


    def cross(self, v2):
        a1 = self.x
        a2 = self.y 
        a3 = self.z
        b1 = v2.x   
        b2 = v2.y
        b3 = v2.z

        x = a2 * b3 - a3 * b2
        y = a3 * b1 - a1*b3
        z = a1*b2 - a2*b1

        return Vector(x,y,z)

    def dot(self, v2):
        return self.x * v2.x +self.y*v2.y + self.z * v2.z

