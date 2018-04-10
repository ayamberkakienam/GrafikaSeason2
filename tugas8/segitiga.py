import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *


verticies = (
    (0, 1, 1),
    (-1, -1, 1),
    (1,-1,1)
    )

edges = (
    (0,1),
    (0,2),
    (1,2)
    )

colors = (
    (1,0,0),
    (0,1,0),
    (0,0,1)
    )

surfaces = (
    (0,1,2),
    )

def Triangle():
    glShadeModel(GL_SMOOTH)
    glBegin(GL_POLYGON)
    x = -1
    for surface in surfaces:
        for vertex in surface:
            x+=1
            glColor3fv(colors[x])
            glVertex3fv(verticies[vertex])
    glEnd()


def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(0.0,0.0, -5)




    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Triangle()
        pygame.display.flip()
        pygame.time.wait(10)

main()


