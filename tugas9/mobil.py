import grafikautils as utils

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from time import sleep

window = 0                                             # glut window number
width, height = 800, 600                               # window size
rotation = 0

def obj_wheel_1():
    x, y = 190, 250
    glColor3f(0.2, 0.2, 0.2)
    utils.draw_circle(x, y, 50, 100, 1)

    glPushMatrix()
    glColor3f(0.8, 0.8, 0.8)
    glTranslatef(x, y, 0)
    glRotatef(rotation, 0, 0, 1)
    glTranslatef(-x, -y, 0)
    utils.draw_circle(x, y, 45, 9, 0)
    utils.draw_circle(x, y, 43, 9, 1)

    glColor3f(0.2, 0.2, 0.2)
    utils.draw_circle(x, y, 20, 8, 1)
    glPopMatrix()

def obj_wheel_2():
    x, y = 500, 250
    glColor3f(0.2, 0.2, 0.2)
    utils.draw_circle(x, y, 50, 100, 1)

    glPushMatrix()
    glColor3f(0.8, 0.8, 0.8)
    glTranslatef(x, y, 0)
    glRotatef(rotation, 0, 0, 1)
    glTranslatef(-x, -y, 0)
    utils.draw_circle(x, y, 45, 9, 0)
    utils.draw_circle(x, y, 43, 9, 1)

    glColor3f(0.2, 0.2, 0.2)
    utils.draw_circle(x, y, 20, 8, 1)
    glPopMatrix()

def obj_body():
    vertices_body = (
        (200, 350),
        (240, 430),
        (560, 430),
        (600, 350),
        (600, 250),
        (90, 250),
        (90, 300),
        (120, 350),
        )
    glShadeModel(GL_SMOOTH)
    glBegin(GL_POLYGON)
    glColor3f(0.6, 0.93, 0.0)
    for vertex in vertices_body:
        glVertex2fv(vertex)
    glEnd()

    vertices_window_1 = (
        (215, 350),
        (250, 420),
        (370, 420),
        (370, 350),
        )

    glBegin(GL_POLYGON)
    glColor3f(1, 1, 1)
    for vertex in vertices_window_1:
        glVertex2fv(vertex)
    glEnd()

def draw():                                            # ondraw is called all the time
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # clear the screen
    glLoadIdentity()                                   # reset position
    utils.refresh2d(width, height)                     # set mode to 2d
       
    obj_body()
    obj_wheel_1()
    obj_wheel_2()

    glutSwapBuffers()                                  # important for double buffering
   
def idle():
    global rotation
    rotation += 2
    glutPostRedisplay()
    
# initialization
glutInit()                                             # initialize glut
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
glutInitWindowSize(width, height)                      # set window size
glutInitWindowPosition(0, 0)                           # set window position
window = glutCreateWindow("noobtuts.com")              # create window with title
glutDisplayFunc(draw)                                  # set draw function callback
glutIdleFunc(idle)                                     # draw all the time
glutMainLoop()                                         # start everything