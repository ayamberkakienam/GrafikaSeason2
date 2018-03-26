import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

xcenter = 0.0
ycenter = 0.0
zcenter = -115

width = 800
height = 600

vertices_body = (
    (-30, 1, 1),
    (-25, 15, 1),
    (25, 15, 1),
    (30, 1, 1),
    (30, -15, 1),
    (-40, -15, 1),
    (-40, 1, 1)
    )

def Triangle():
    glShadeModel(GL_SMOOTH)
    glBegin(GL_POLYGON)
    glColor3fv((1, 1, 1))
    for vertex in vertices_body:
        glVertex3fv(vertex)
    glEnd()

vertices_wheel = (
    (-30, -30, 1),
    (-10, -30, 1),
    (-10, -10, 1),
    (-30, -10, 1),
    )

def Wheel():
    glShadeModel(GL_SMOOTH)
    glBegin(GL_POLYGON)
    glColor3fv((1, 1, 1))
    for vertex in vertices_wheel:
        glVertex3fv(vertex)
    glEnd()    



def refresh2d(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, width, 0.0, height, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def draw():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    refresh2d(width, height)
    Wheel()
    glutSwapBuffers()

def main():
    # pygame.init()
    # pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    
    # glutInit()
    # gluPerspective(45, (display[0]/display[1]), 0.1, 120)
    # glutDisplayFunc(draw)
    # glutIdleFunc(draw)
    # glutMainLoop()
    
    # initialization
    glutInit()                                             # initialize glut
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
    glutInitWindowSize(width, height)                      # set window size
    glutInitWindowPosition(0, 0)                           # set window position
    window = glutCreateWindow("Tugas Grafika")             # create window with title
    glutDisplayFunc(draw)                                  # set draw function callback
    glutIdleFunc(draw)                                     # draw all the time
    glutMainLoop()                                         # start everything



    # x = 0
    # while True:
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             pygame.quit()
    #             quit()
    #     glTranslatef(xcenter, ycenter, zcenter)
    #     Triangle()
    #     Wheel()
    #     glRotatef(1, 0, 0, 1)
    #     glTranslatef(-xcenter, -ycenter, -zcenter)
    #     pygame.display.flip()
    #     pygame.time.wait(10)

main()


