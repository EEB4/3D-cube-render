import pygame as pg
import numpy as np
from math import *
from array import *


WIDTH, HEIGHT = 800, 600
pg.display.set_caption("3d cube")
screen = pg.display.set_mode((WIDTH, HEIGHT))

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

SCALE = 100
POS = [WIDTH/2, HEIGHT/2]

mousepos = array('i', pg.mouse.get_pos())

anglez = 0
angley = 5
anglex = 3


#start points array
points = []
#generating matrix array
points.append(np.matrix([-1, -1, 1]))
points.append(np.matrix([1, -1, 1]))
points.append(np.matrix([1,  1, 1]))
points.append(np.matrix([-1, 1, 1]))
points.append(np.matrix([-1, -1, -1]))
points.append(np.matrix([1, -1, -1]))
points.append(np.matrix([1, 1, -1]))
points.append(np.matrix([-1, 1, -1]))


projection_matrix = np.matrix([
    [1, 0, 0],
    [0, 1, 0],
])



clock = pg.time.Clock()
while True:

    clock.tick(60)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                pg.quit()
                exit()

    #update

    rotation_z = np.matrix([
        [cos(anglez), -sin(anglez), 0],
        [sin(anglez), cos(anglez), 0],
        [0, 0, 1],
    ])
    rotation_y = np.matrix([
        [cos(angley), 0, sin(angley)],
        [0, 1, 0],
        [-sin(angley), 0, cos(angley)],
    ])

    rotation_x = np.matrix([
        [1, 0, 0],
        [0, cos(anglex), -sin(anglex)],
        [0, sin(anglex), cos(anglex)],
    ])


    #automatic movement
    anglex += 0.01
    angley += 0.01
    anglez += 0.01


    #mouse based movement
    #mousepos = array('f', pg.mouse.get_pos())
    #anglez = 180
    #angley = (mousepos[0]/360) +180
    #anglex = (mousepos[1]/360) + 3

    screen.fill(WHITE)


    #draw

    for point in points:
        rotated2d = np.dot(rotation_y, point.reshape((3, 1)))
        rotated2d = np.dot(rotation_x, rotated2d)
        #rotated2d = np.dot(rotation_x, rotated2d)

        projected2d = np.dot(projection_matrix, rotated2d)

        x = int(projected2d[0][0]*SCALE) + POS[0]
        y = int(projected2d[1][0]*SCALE) + POS[1]
        pg.draw.circle(screen, BLACK, (x, y), 5)


    pg.display.update()