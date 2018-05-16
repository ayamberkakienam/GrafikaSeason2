# Basic OBJ file viewer. needs objloader from:
#  http://www.pygame.org/wiki/OBJFileLoader
# LMB + move: rotate
# RMB + move: pan
# Scroll wheel: zoom in/out
import sys, pygame, random
import grafikautils as utils
from pygame.locals import *
from pygame.constants import *
from OpenGL.GL import *
from OpenGL.GLU import *
from ctypes import *

# IMPORT OBJECT LOADER
from objloader import *

white = (1,1,1)
black = (0,0,0)
grey = (0.5,0.5,0.5)
blue = (0.23,0.52,1)
brown = (0.98,0.63,0.098)

class Particle():
    def __init__(self, startx, starty, startz, col):
        self.x = startx
        self.y = starty
        self.z = startz
        self.col = col
        self.sx = startx
        self.sy = starty
        self.sz = startz

    def move(self):
        if self.y < -10:
            self.x=self.sx
            self.y=self.sy
            self.z=self.sz

        else:
            self.y-=random.uniform(0.2, 0.7)

        self.x+=random.uniform(-0.1, 0.1)
        # self.z+=random.uniform(-0.1, 0.1)

class ParticleHujan():
    def __init__(self,startz):
        self.x = random.uniform(-5,5)
        self.y = random.uniform(-5,5)
        self.z = startz
        self.col = blue
        self.sx = self.x
        self.sy = self.y
        self.sz = startz
        self.draw = True

    def move(self,windx,windy):
        if (self.z < 1):
            self.draw = False
        else:
            self.z = self.z - 0.15
            self.x = self.x + windx
            self.y = self.y + windy

    def isDraw(self):
        return self.draw

    def returnStart(self):
        self.x = self.sx
        self.y = self.sy
        self.z = self.sz
        self.draw = True

pygame.init()
viewport = (800,600)
hx = viewport[0]/2
hy = viewport[1]/2
srf = pygame.display.set_mode(viewport, OPENGL | DOUBLEBUF)
intensity = 0.1
glLightfv(GL_LIGHT0, GL_POSITION,  (-40, 200, 100, 0.0))
glLightfv(GL_LIGHT0, GL_AMBIENT, (intensity, intensity, intensity, 1.0))
glLightfv(GL_LIGHT0, GL_DIFFUSE, (0.5, 0.5, 0.5, 1.0))
glEnable(GL_LIGHT0)
glEnable(GL_LIGHTING)
glEnable(GL_COLOR_MATERIAL)
glEnable(GL_DEPTH_TEST)
glEnableClientState (GL_VERTEX_ARRAY)
glShadeModel(GL_SMOOTH)           # most obj files expect to be smooth-shaded

# LOAD OBJECT AFTER PYGAME INIT
obj = OBJ(sys.argv[1], swapyz=True)

clock = pygame.time.Clock()

glMatrixMode(GL_PROJECTION)
glLoadIdentity()
width, height = viewport
gluPerspective(90.0, width/float(height), 1, 100.0)
glEnable(GL_DEPTH_TEST)
glMatrixMode(GL_MODELVIEW)

rx, ry = (0,0)
tx, ty = (0,0)
zpos = 5
rotate = move = False

particles = []
hujan = []

for part in range(300):
    r = random.uniform(0.0, 1.0)
    g = random.uniform(0.0, 1.0)
    b = random.uniform(0.0, 1.0)
    col = (r,g,b)
    particles.append( Particle(0, -2.2, 0, col) )

for part in range(200):
    ssz = 0.5 + part
    temp = ParticleHujan(ssz)
    hujan.append(temp)

# vertices = [ 0.0, 1.0, 0.0,  0.0, 0.0, 0.0,  1.0, 1.0, 0.0 ]
# vbo = glGenBuffers (1)
# glBindBuffer (GL_ARRAY_BUFFER, vbo)
# glBufferData (GL_ARRAY_BUFFER, len(vertices)*4, (c_float*len(vertices))(*vertices), GL_STATIC_DRAW)

px, py = (tx/20, ty/20)
windx = 0
windy = 0

while 1:
    print "fps:", clock.get_fps()
    clock.tick()
    
    # srf.fill(white)
    for e in pygame.event.get():
        if e.type == QUIT:
            sys.exit()
        elif e.type == KEYDOWN and e.key == K_ESCAPE:
            sys.exit()
        elif e.type == MOUSEBUTTONDOWN:
            if e.button == 4: zpos = max(1, zpos-1)
            elif e.button == 5: zpos += 1
            elif e.button == 1: rotate = True
            elif e.button == 3: move = True
        elif e.type == MOUSEBUTTONUP:
            if e.button == 1: rotate = False
            elif e.button == 3: move = False
        elif e.type == MOUSEMOTION:
            i, j = e.rel
            if rotate:
                rx += i
                ry += j
            if move:
                tx += i
                ty -= j
        elif e.type == KEYDOWN and e.key == K_UP and intensity < 1:
            intensity += 0.1
        elif e.type == KEYDOWN and e.key == K_DOWN and intensity > -1:
            intensity -= 0.1
        elif e.type == KEYDOWN and e.key == K_w and windx < 1:
            windx = windx + 0.01
        elif e.type == KEYDOWN and e.key == K_s and windx > -1:
            windx = windx - 0.01
        elif e.type == KEYDOWN and e.key == K_d and windy < 1:
            windy = windy + 0.01
        elif e.type == KEYDOWN and e.key == K_a and windy > -1:
            windy = windy - 0.01



    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    # RENDER OBJECT
    glTranslate(tx/20., ty/20., - zpos)
    glLightfv(GL_LIGHT0, GL_AMBIENT, (intensity, intensity, intensity, 1.0))
    glRotate(-90, 1, 0, 0)
    glRotate(ry, 1, 0, 0)
    glRotate(rx, 0, 0, 1)
    glCallList(obj.gl_list)

    for p in particles:
        p.move()
        # glTranslate(p.x, p.y, - zpos)
        # glBindBuffer (GL_ARRAY_BUFFER, vbo)
        # glVertexPointer (3, GL_FLOAT, 0, None)
        # glDrawArrays (GL_TRIANGLES, 0, 3)
        # utils.draw_circle(p.x, p.y, 0.05, 100, True)
        glColor3f(p.col[0], p.col[1], p.col[2])
        utils.draw_cube(p.x, p.y, p.z)

    for h in hujan:
        if h.isDraw():
            h.move(windx,windy)
            glColor3f(h.col[0], h.col[1], h.col[2])
            utils.draw_line_hujan(h.x, h.y, h.z, 0.2, windx, windy)            
        else:
            h.returnStart()

        


    pygame.display.flip()

# TODO:
#   - naikin z starting position dari asep
#   - bikin atribut pos z
#   - 3d particle?