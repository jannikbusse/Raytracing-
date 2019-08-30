import numpy as np
import pygame
import Vector

class Sphere(object):
    center = Vector.Vector()
    radius = 0

    color = (0,255,0)

    def __init__(self, center, radius, color = (0,255,0)):
        self.center = center
        self.radius = radius
        self.color = color

    def __init__(self, center, radius, color = (0,255,0)):
        x,y,z = center
        self.center = Vector.Vector(x,y,z)
        self.radius = radius
        self.color = color    

    def getImplicitMatrix(self):
        matrix = np.array([[1,0,0,-self.center.x],
                          [0,1,0, -self.center.y],
                          [0,0,1, -self.center.z],
                          [-self.center.x, -self.center.y, -self.center.z, (self.center.x*self.center.x
                           + self.center.y*self.center.y 
                           + self.center.z*self.center.z 
                           - self.radius*self.radius)]])
        return matrix

  