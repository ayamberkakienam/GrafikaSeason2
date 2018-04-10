import OpenGL.GL as GL
import glm
import OpenGL.GL.shaders
from OpenGL.GLU import *
from OpenGL.GLUT import *
import ctypes
import pygame
import numpy
from math import *

transform1 = 0.0
transform2 = 0.0
transform3 = 0.0
transform4 = 0.0
transform5 = 0.0

def get_vertex_shader(inp):
    return "#version 330\n layout (location = 0) in vec4 position; layout (location = 1) in vec2 aTexCoord; uniform float transform"+str(inp)+";out vec2 TexCoord;void main(){gl_Position = vec4(position.x + transform"+str(inp)+", position.y, 0.0, 1.0);TexCoord = vec2(aTexCoord.x, aTexCoord.y);}"

def get_fragment_shader(a, b, c, d):
    return "#version 330\n void main(){gl_FragColor = vec4("+str(a)+"f, "+str(b)+"f, "+str(c)+"f, "+str(d)+"f);}"

def ban(x, y):
    radius = 0.1
    posx = x
    posy = y
    sides = 360
    edges = []

    # glBegin(GL_POLYGON)
    # glColor3fv((0,0,1))
    hasil_ban = []
    for i in range(sides):
        posx_cosine = radius * cos((360-i)*2*pi/sides) + posx
        posy_sines = radius * sin((360-i)*2*pi/sides) + posy
        # glVertex2fv((posx_cosine, posy_sines))
        hasil_ban.append(posx_cosine)
        hasil_ban.append(posy_sines)
        hasil_ban.append(0)
        hasil_ban.append(1)
    # glEnd()
    return hasil_ban

vertices = [
        -2.1, 0, 0, 1,
        -2.1, 1, 0, 1,
        -2, 1, 0, 1,
        -2, 0.3, 0, 1,
        -1.70, 0.3, 0, 1,
        -1.70, 0, 0, 1,
        # (0,1),
        # (1,1),
        # (1,0),
]


vertices2 = [
    -3.0, 0, 0, 1,
    -3,0.3,0,1,
    -0.7,0.3,0,1,
    -0.7,0.7,0,1,
    0,0.7,0,1,
    0,0.3,0,1,
    0.4,0.3,0,1,
    0.4,0.9,0,1,
    0.5,0.9,0,1,
    0.5,0.3,0,1,
    3,0.3,0,1,
    3,0,0,1
]

jalan = [
    -1,0,0,1,
    1,0,0,1,
    1,-1,0,1,
    -1,-1,0,1,
]
##GANTI
mobil =
            -0.1, 0.1, 0, 1,
            0.1, 0.1, 0, 1,
            0.2, -0.1, 0, 1,
            0.4, -0.1, 0, 1,
             0.4, -0.3, 0, 1,
            -0.4, -0.3, 0, 1,
            -0.4, -0.1, 0, 1,
            -0.2, -0.1, 0, 1
]

vertices3 = [
        -1, -1, 0, 1,
        -1, -0.5, 0, 1,
        1, -0.5, 0, 1,
        1, -1, 0, 1
]

ban1 = ban(-0.2, -0.4)
ban2 = ban(0.2, -0.4)

vertices = numpy.array(vertices, dtype=numpy.float32)
vertices2 = numpy.array(vertices2, dtype=numpy.float32)
jalan = numpy.array(jalan, dtype=numpy.float32)
mobil = numpy.array(mobil, dtype=numpy.float32)
vertices3 = numpy.array(vertices3, dtype=numpy.float32)
ban1 = numpy.array(ban1, dtype=numpy.float32)
ban2 = numpy.array(ban2, dtype=numpy.float32)

def create_object(shader, datas):
    
    # Create a new VAO (Vertex Array Object) and bind it
    vertex_array_object = GL.glGenVertexArrays(1)
    GL.glBindVertexArray( vertex_array_object )
    
    # Generate buffers to hold our vertices
    vertex_buffer = GL.glGenBuffers(1)
    GL.glBindBuffer(GL.GL_ARRAY_BUFFER, vertex_buffer)
    
    # Get the position of the 'position' in parameter of our shader and bind it.
    position = GL.glGetAttribLocation(shader, 'position')
    #GL.glEnableVertexAttribArray(position)
    GL.glEnableVertexAttribArray(position)

    # Describe the position data layout in the buffer
    GL.glVertexAttribPointer(position, 4, GL.GL_FLOAT, False, 0, ctypes.c_void_p(0))
    
    # Send the data over to the buffer
    GL.glBufferData(GL.GL_ARRAY_BUFFER, 4 * len(datas), datas, GL.GL_STATIC_DRAW)
    #GL.glBufferData(GL.GL_ARRAY_BUFFER, 48, vertices2, GL.GL_STATIC_DRAW)
    # Unbind the VAO first (Important)
    GL.glBindVertexArray(0)
    
    # Unbind other stuff
    GL.glDisableVertexAttribArray(position)
    GL.glBindBuffer(GL.GL_ARRAY_BUFFER, 0)
    
    return vertex_array_object
    
def display(shader, vertex_array_object):
    global transform1, transform2, transform3, transform4, transform5

    GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)
    # GL.glUseProgram(shader[0])
    
    # transLoc = GL.glGetUniformLocation(shader[0], "transform")
    # GL.glUniform1f(transLoc, transform)
    # transform += 0.0001

    # GL.glBindVertexArray( vertex_array_object[0] )
    # GL.glDrawArrays(GL.GL_POLYGON, 0, 5)
    # GL.glBindVertexArray( 0 )
    # GL.glUseProgram(0)
#ban1
    GL.glUseProgram(shader[6])
    transLoc = GL.glGetUniformLocation(shader[5], "transform3")
    GL.glBindVertexArray(vertex_array_object[5])
    GL.glUniform1f(transLoc, transform3)
    GL.glDrawArrays(GL.GL_POLYGON, 0, len(ban1) // 4)
    GL.glBindVertexArray(1)
    GL.glUseProgram(0)
    #end

    #ban2
    GL.glUseProgram(shader[6])
    transLoc = GL.glGetUniformLocation(shader[6], "transform4")
    GL.glUniform1f(transLoc, transform4)
    GL.glBindVertexArray(vertex_array_object[6])
    GL.glDrawArrays(GL.GL_POLYGON, 0, len(ban2) // 4)
    GL.glBindVertexArray(1)
    GL.glUseProgram(0)
    #end


    #gambar mobil
    GL.glUseProgram(shader[4])
    transLoc = GL.glGetUniformLocation(shader[4], "transform3")
    GL.glUniform1f(transLoc, transform3)
    GL.glBindVertexArray( vertex_array_object[3] )
    GL.glDrawArrays(GL.GL_POLYGON, 0, len(mobil)//4)
    GL.glBindVertexArray( 1 )
    GL.glUseProgram(0)
    #end

    # border jalan
    GL.glUseProgram(shader[3])
    transLoc = GL.glGetUniformLocation(shader[3], "transform3")
    GL.glUniform1f(transLoc, transform3)
    GL.glBindVertexArray(vertex_array_object[4])
    GL.glDrawArrays(GL.GL_POLYGON, 0, len(vertices3) // 4)
    GL.glBindVertexArray(1)
    GL.glUseProgram(0)
    #end

    # gambar gedung
    GL.glUseProgram(shader[1])
    transLoc = GL.glGetUniformLocation(shader[1], "transform2")
    GL.glUniform1f(transLoc, transform2)
    transform2 -= 0.001
    if (transform2 < -2):
        transform2 = 2
    GL.glBindVertexArray( vertex_array_object[1] )
    GL.glDrawArrays(GL.GL_POLYGON, 0, 12)
    GL.glBindVertexArray( 1 )
    GL.glUseProgram(0)
    #end
    
    #gambar background hitam buat jalan
    GL.glUseProgram(shader[2])
    transLoc = GL.glGetUniformLocation(shader[2], "transform2")
    GL.glUniform1f(transLoc, transform1)
    GL.glBindVertexArray( vertex_array_object[2] )
    GL.glDrawArrays(GL.GL_POLYGON, 0, 4)
    GL.glBindVertexArray( 1 )
    GL.glUseProgram(0)
    #end

    

def main():
    global vertices
    global vertices2
    
    global jalan 
    global vertices3
    global ban1
    global ban2

    pygame.init()
    screen = pygame.display.set_mode((800, 600), pygame.OPENGL|pygame.DOUBLEBUF)
    GL.glClearColor(0, 1, 1, 1.0)
    GL.glEnable(GL.GL_DEPTH_TEST)

    shader = OpenGL.GL.shaders.compileProgram(
        OpenGL.GL.shaders.compileShader(get_vertex_shader(1), GL.GL_VERTEX_SHADER),
        OpenGL.GL.shaders.compileShader(get_fragment_shader(1.0, 1.0, 1.0, 1.0), GL.GL_FRAGMENT_SHADER)
    )

    shader2 = OpenGL.GL.shaders.compileProgram(
        OpenGL.GL.shaders.compileShader(get_vertex_shader(2), GL.GL_VERTEX_SHADER),
        OpenGL.GL.shaders.compileShader(get_fragment_shader(0.0, 0.0, 0.3, 0.0), GL.GL_FRAGMENT_SHADER)
    )

    jalanShader = OpenGL.GL.shaders.compileProgram(
        OpenGL.GL.shaders.compileShader(get_vertex_shader(2), GL.GL_VERTEX_SHADER),
        OpenGL.GL.shaders.compileShader(get_fragment_shader(0.0, 0.0, 0.0, 0.0), GL.GL_FRAGMENT_SHADER)
    )

    shader3 = OpenGL.GL.shaders.compileProgram(
        OpenGL.GL.shaders.compileShader(get_vertex_shader(3), GL.GL_VERTEX_SHADER),
        OpenGL.GL.shaders.compileShader(get_fragment_shader(1.0, 1.0, 1.0, 1.0), GL.GL_FRAGMENT_SHADER)
    )

    shaderMobil = OpenGL.GL.shaders.compileProgram(
        OpenGL.GL.shaders.compileShader(get_vertex_shader(3), GL.GL_VERTEX_SHADER),
        OpenGL.GL.shaders.compileShader(get_fragment_shader(0.5, 0.5, 0.5, 1.0), GL.GL_FRAGMENT_SHADER)
    )
    
    shader4 = OpenGL.GL.shaders.compileProgram(
        OpenGL.GL.shaders.compileShader(get_vertex_shader(4), GL.GL_VERTEX_SHADER),
        OpenGL.GL.shaders.compileShader(get_fragment_shader(1.0, 0.0, 0.0, 1.0), GL.GL_FRAGMENT_SHADER)
    )

    shader5 = OpenGL.GL.shaders.compileProgram(
        OpenGL.GL.shaders.compileShader(get_vertex_shader(5), GL.GL_VERTEX_SHADER),
        OpenGL.GL.shaders.compileShader(get_fragment_shader(1.0, 0.0, 0.0, 1.0), GL.GL_FRAGMENT_SHADER)
    )

    shaders = []
    shaders.append(shader)
    shaders.append(shader2)
    shaders.append(jalanShader)
    shaders.append(shader3)
    shaders.append(shaderMobil)

    shaders.append(shader4)
    shaders.append(shader5)
    clock = pygame.time.Clock()
    
    while True:
        vertex_array_object = []
        vertex_array_object.append(create_object(shader, vertices))
        vertex_array_object.append(create_object(shader2, vertices2))  
        vertex_array_object.append(create_object(jalanShader,jalan))   
        vertex_array_object.append(create_object(shader3, mobil))
        vertex_array_object.append(create_object(shader3, vertices3))
        vertex_array_object.append(create_object(shader4, ban1))
        vertex_array_object.append(create_object(shader5, ban2))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE:
                return
        
        display(shaders, vertex_array_object)
        # vertices[0] += 0.001
        # vertices2[4] -= 0.001
            

        pygame.display.flip()

if __name__ == '__main__':
    try:
        main()
    finally:
        pygame.quit()