import pygame
import numpy as np
import Sphere
import Vector
import Ray
import random
from PIL import Image
import Camera

spheres = []
xDIM = 500
yDIM = 500
zDim = 500
camera = Camera.Camera(xDIM,yDIM)



for i in range(10):
    x = (random.randint(1,xDIM))
    y = (random.randint(1,yDIM))
    z = (random.randint(1,zDim))

    r = (random.randint(1,100))
    s = Sphere.Sphere((x,y,z),r)
    spheres.append(s)

img = Image.new('RGB', (xDIM, xDIM), color = 'red')
print(img.getpixel((20,20)))
for x in range(xDIM):
    for y in range(yDIM):
        img.putpixel((x,y), camera.getPixel(x,y, spheres))
img.save('pil_red.png')


