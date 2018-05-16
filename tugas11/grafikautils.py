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
    glVertex2f(x, y)                                   # bottom left point
    glVertex2f(x + width, y)                           # bottom right point
    glVertex2f(x + width, y + height)                  # top right point
    glVertex2f(x, y + height)                          # top left point
    glEnd()

def draw_line_hujan(x,y,z,len,windx,windy):
	glBegin(GL_LINES)
	finx = x + windx
	finy = y + windy
	finz = z + len
	glVertex3f(x,y,z)
	glVertex3f(finx,finy,finz)
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

def draw_cube(x, y, z):
	sf = 0.05
	rf = 1/sf

	vertices= (
	    (sf, -sf, -sf),
	    (sf, sf, -sf),
	    (-sf, sf, -sf),
	    (-sf, -sf, -sf),
	    (sf, -sf, sf),
	    (sf, sf, sf),
	    (-sf, -sf, sf),
	    (-sf, sf, sf)
    	)

	edges = (
		(0,1),
		(0,3),
		(0,4),
		(2,1),
		(2,3),
		(2,7),
		(6,3),
		(6,4),
		(6,7),
		(5,1),
		(5,4),
		(5,7)
		)

	glTranslatef(x, y, z)
	glBegin(GL_LINES)
	for edge in edges:
		for vertex in edge:
			glVertex3fv(vertices[vertex])
	glEnd()
	glTranslatef(-x, -y, 0)