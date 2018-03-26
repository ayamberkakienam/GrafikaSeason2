from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

import math

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

def draw_circle(cx, cy, r, num_segments, filled):
	theta = 2 * 3.1415926 / num_segments
	c = math.cos(theta)
	s = math.sin(theta)

	x = r
	y = 0

	if filled:
		mode = GL_POLYGON
	else:
		mode = GL_LINE_LOOP

	glBegin(mode)

	for ii in xrange(0,num_segments):
		glVertex2f(x+cx, y+cy)

		# apply the rotation
		t = x
		x = c*x-s*y
		y = s*t+c*y

	glEnd()