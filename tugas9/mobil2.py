import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
from math import *

titik_sudut = (
    (-2, 3),
    (2, 3),
    (3, 0),
    (6, 0),
    (6, -3),
    (-6, -3),
    (-6, 0),
    (-3, 0),
)

sisi_sisi = (
    (1, 2),
    (2, 3),
    (3, 4),
    (4, 5),
    (5, 6),
    (6, 7),
    (7, 0),
    (0, 1),
)

permukaan = (
    (1, 2, 3, 4, 5, 6, 7),
)



def mobil():
    glBegin(GL_POLYGON)
    glColor3fv((0, 1, 0))
    for sisi in sisi_sisi:
        for sudut in sisi:
            glVertex2fv(titik_sudut[sudut])
    glEnd()


def ban(x, y):
    radius = 2
    posx = x
    posy = y
    sides = 360
    edges = []

    glBegin(GL_POLYGON)
    glColor3fv((0,0,1))
    for i in range(sides):
        posx_cosine = radius * cos(i*2*pi/sides) + posx
        posy_sines = radius * sin(i*2*pi/sides) +posy
        glVertex2fv((posx_cosine, posy_sines))
    glEnd()

    glBegin(GL_LINES)
    titik_titik = [(posx, posy), (posx+radius, posy)]
    edges = [(0, 1)]
    for i in range(1, sides):
        if i % 60 == 0:
            posx_cosine = radius * cos(i * 2 * pi / sides) + posx
            posy_sines = radius * sin(i * 2 * pi / sides) + posy
            titik_titik.append((posx_cosine, posy_sines))
            edges.append((0, i//60 + 1))

    for sisi in edges:
        for sudut in sisi:
            glVertex2fv(titik_titik[sudut])
            glColor3fv((1, 1, 1))
    glEnd()

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(-30, 0, -50)

    glRotatef(1, 0, 0, 0)

    sudut = [0]
    # glEnable(GL_DEPTH_TEST)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        mobil()

        glPushMatrix()
        glTranslatef(-3, -4.5, 0)
        glRotatef(sudut[0], 0.0, 0.0, 1.0)
        ban(0, 0)
        glTranslatef(3, 4.5, 0)
        glPopMatrix()

        glPushMatrix()
        glTranslatef(4, -4.5, 0)
        glRotatef(sudut[0], 0.0, 0.0, 1.0)
        ban(0, 0)
        glTranslatef(-4, 4.5, 0)
        glPopMatrix()

        sudut[0] += 15
        glTranslatef(0.2,0,0)
        pygame.display.flip()
        pygame.time.wait(10)

main()


















