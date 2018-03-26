from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from time import sleep

window = 0                                             # glut window number
width, height = 800, 600                               # window size

def refresh2d(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    glOrtho(0.0, width, 0.0, height, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def draw_rect(x, y, width, height):
    glBegin(GL_QUADS)                                  # start drawing a rectangle
    glColor3f(0.0, 0.0, 1.0)                           # set color to blue
    glVertex2f(x, y)                                   # bottom left point
    glVertex2f(x + width, y)                           # bottom right point
    glVertex2f(x + width, y + height)                  # top right point
    glVertex2f(x, y + height)                          # top left point
    glEnd()

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
    glColor3fv((1, 1, 1))
    for vertex in vertices_body:
        glVertex2fv(vertex)
    glEnd()

x = 10
def draw():                                            # ondraw is called all the time
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # clear the screen
    glLoadIdentity()                                   # reset position
    refresh2d(width, height)                           # set mode to 2d
       
    # obj_wheel()
    obj_body()
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