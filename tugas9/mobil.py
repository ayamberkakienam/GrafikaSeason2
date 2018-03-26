import grafikautils as utils

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from time import sleep

window = 0                                             # glut window number
width, height = 800, 600                               # window size

vertices_wheel = (
    (300, 300),
    (100, 300),
    (100, 100),
    (300, 100),
    (400, 400)
    )

def obj_wheel():
    glPushMatrix()
    # glRotate(x, 0, 0, 1)
    glBegin(GL_POLYGON)
    glColor3f(1, 1, 1)
    for vertex in vertices_wheel:
        glVertex2fv(vertex)
    glEnd()  
    glPopMatrix()

vertices_body = ( # +230, +350
    (200, 350),
    (240, 430),
    (560, 430),
    (600, 350),
    (600, 250),
    (90, 250),
    (90, 300),
    (120, 350),
    )

def obj_body():
    glShadeModel(GL_SMOOTH)
    glBegin(GL_POLYGON)
    glColor3fv((0.5, 0.8, 0.2))
    for vertex in vertices_body:
        glVertex2fv(vertex)
    glEnd()

x = 10
def draw():                                            # ondraw is called all the time
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # clear the screen
    glLoadIdentity()                                   # reset position
    utils.refresh2d(width, height)                           # set mode to 2d
       
    # obj_wheel()
    obj_body()
    utils.draw_circle(100, 100, 50, 100, 0)
    # draw_rect(100, 100, 200, 100)                        # rect at (10, 10) with width 200, height 100
        

    glutSwapBuffers()                                  # important for double buffering
   
def idle():
    global x
    x += 10
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