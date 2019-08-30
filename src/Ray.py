import numpy as np
import pygame
import Vector
import Sphere

class Ray(object):
    origin = Vector.Vector()
    dir = Vector.Vector()
    bounces = 0

    def __init__(self, origin, dir):
        self.origin = origin
        self.dir = dir

    def __init__(self, origin, dir):
        o1,o2,o3 = origin
        d1,d2,d3 = dir
        self.origin = Vector.Vector(o1, o2, o3)
        self.dir = Vector.Vector(d1,d2,d3)

    def intersects(self, sphere):
        origin = self.origin
        dir = self.dir
        cross = self.dir.cross(sphere.center.sub(self.origin))
        d = cross.len()
        if d < sphere.radius:

            t = self.dir.dot(sphere.center.sub(self.origin))

            
            xp = np.sqrt(sphere.radius*sphere.radius -(d * d))
            xm = -np.sqrt(sphere.radius*sphere.radius -(d * d))

           



            p1 = self.dir.scale(t+xp)
            p2 = self.dir.scale(t+xm)

            if p1.dst(origin) < p2.dst(origin):
                return (True, p1)
            else :
                return (True, p2)

        elif d == sphere.radius:
            return(True, cross)

        return (False, dir)

    def cast(self, origin, dir, spheres):
        o1,o2,o3 = origin
        d1,d2,d3 = dir
        self.origin = Vector.Vector(o1,o2,o3)
        self.dir = Vector.Vector(d1,d2,d3)

        color = (0,0,0)
        for sphere in spheres:
            b, i = self.intersects(sphere)
            if b:
                color = sphere.color
                print(color)
                print(b)
           
        return color


    def castOld(self, spheres):
        color = (0,0,0)
        for sphere in spheres:
            b, i = self.intersects(sphere)
            if b:
                color = sphere.color
           
        return color


