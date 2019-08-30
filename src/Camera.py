import numpy as np
import pygame
import Vector
import Ray

class Camera:

    xDim = 0
    yDim = 0
    ray = Ray.Ray((0,0,0),(0,0,0))


    def __init__(self, xDim,yDim):
        self.xDim = xDim
        self.yDim = yDim
   
   
    def getPixel(self, x, y, spheres):
       return self.ray.cast((x,y,0),(0,0,1), spheres)

