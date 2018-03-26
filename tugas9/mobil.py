import grafikautils as utils

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

import random
from time import sleep

window = 0                                             # glut window number
width, height = 800, 600                               # window size
rotation = 0
# t = 0
# t_a = list()

weather_r = 0.35
weather_g = 0.5
weather_b = 1
day = 1

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

def obj_road():
    road_width = 280
    vertices_road = (
        (0, 0),
        (0, road_width),
        (width, road_width),
        (width, 0),
        )

    glShadeModel(GL_SMOOTH)
    glBegin(GL_POLYGON)
    glColor3f(0.2, 0.2, 0.2)
    for vertex in vertices_road:
        glVertex2fv(vertex)
    glEnd()

def obj_town():
    building_width = 100

    glColor3f(0.1, 0.3, 0)
    for i in range(0, 20, 10):
        building_height = random.uniform(40, 100)
        utils.draw_rect(i*building_width+2, 280, building_width, building_height)


def draw():                                            # ondraw is called all the time
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # clear the screen
    glLoadIdentity()                                   # reset position
    utils.refresh2d(width, height)                     # set mode to 2d
    
    glClearColor(weather_r, weather_g, weather_b, 1)

    obj_town()
    obj_road()
    obj_body()
    obj_wheel_1()
    obj_wheel_2()

    glutSwapBuffers()                                  # important for double buffering

def dayNightCycle():
    global weather_g
    global weather_r
    global weather_b
    global day

    change_speed = 0.005
    delay = 0.2
    buff = 0

    # if weather_r > 0.35:
    #     weather_r = 0.35+change_speed
    # if weather_g > 0.5:
    #     weather_g = 0.5+change_speed
    # if weather_b > 1:
    #     weather_b = 1+change_speed

    if weather_r > 0.35+delay and weather_g > 0.5+delay and weather_b > 1+delay:
        day = 1

    if weather_r < 0 and weather_g < 0 and weather_b < 0:
        day = 0

    if day:
        weather_r -= change_speed
        weather_g -= change_speed
        weather_b -= change_speed
    else:
        weather_r += change_speed
        weather_g += change_speed
        weather_b += change_speed

def idle():
    global rotation
    global t
    rotation += 2
    # t_a.append(t)
    dayNightCycle()
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