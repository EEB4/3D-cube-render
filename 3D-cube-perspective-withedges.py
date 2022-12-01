import pygame as pg
import numpy as np
from math import *
from array import *


WIDTH, HEIGHT = 800, 600
pg.display.set_caption("3d cube")
screen = pg.display.set_mode((WIDTH, HEIGHT))

POS = [WIDTH/2, HEIGHT/2]

WHITE = (255, 255, 255)

mousepos = array('i', pg.mouse.get_pos())

anglez = 0
angley = 0
anglex = 0


#initialising points array
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
    [0, 0, 1],
])

projected_points = [
    [n, n] for n in range(len(points))
]


def connect_points(i, j, points):
    pg.draw.line(
        screen, BLACK, (points[i][0], points[i][1]), (points[j][0], points[j][1]))




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

    #anglex += 0.01
    #angley += 0.01
    #anglez += 0.01
    mousepos = array('f', pg.mouse.get_pos())
    anglez = 180
    angley = -(mousepos[0]*4/WIDTH-3.5)
    anglex = (mousepos[1]/HEIGHT*2-1)



    screen.fill(WHITE)


    #draw

    i = 0
    for point in points:
        rotated2d = np.dot(rotation_y, point.reshape((3, 1)))
        rotated2d = np.dot(rotation_x, rotated2d)
        #rotated2d = np.dot(rotation_x, rotated2d)

        projected2d = np.dot(projection_matrix, rotated2d)


        SCALE = 500
        x = int((projected2d[0][0]/(projected2d[2][0] + 3)) * SCALE + POS[1])
        y = int((projected2d[1][0]/(projected2d[2][0] + 3)) * SCALE + POS[1])


        BLACK = (0, 0 ,0)
        projected_points[i] = [x, y]
        #BLACK = (100*(projected2d[2][0] + 1)**2, 100*(projected2d[2][0] + 1)**2, 100*(projected2d[2][0] + 1)**2)

        pg.draw.circle(screen, BLACK, (x, y), 5)
        i += 1


        for p in range(4):
            connect_points(p, (p+1) % 4, projected_points)
            connect_points(p+4, ((p+1) % 4) + 4, projected_points)
            connect_points(p, (p+4), projected_points)


    pg.display.update()