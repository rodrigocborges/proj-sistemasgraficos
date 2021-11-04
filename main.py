import glfw
from OpenGL.GL import *
import numpy as np
import pyrr

from window import Window

#Alguns exemplos: https://github.com/Somsubhra/pyOpenGL-Samples


def frustum(l, r, b, t, n, f):
    elem1 = (2*n)/(r-l)
    elem2 = (2*n)/(t-b)
    A = (r+l)/(r-l)
    B = (t+b)/(t-b)
    C = -(f+n)/(f-n)
    D = -(2*f*n)/(f-n)
    matrix = [[elem1, 0,  A,  0],
              [0, elem2,  B,  0],
              [0,     0,  C,  D],
              [0,     0, -1,  0]]
    matrix = np.transpose(matrix)
    return glMultMatrixf(matrix)


def ortho(l, r, b, t, n, f):
    elem1 = 2.0/(r-l)
    elem2 = 2.0/(t-b)
    elem3 = -2.0/(f-n)
    tx = -(r+l)/(r-l)
    ty = -(t+b)/(t-b)
    tz = -(f+n)/(f-n)
    matrix = [[elem1, 0, 0, tx],
              [0, elem2, 0, ty],
              [0, 0, elem3, tz],
              [0, 0,     0, 1]]
    matrix = np.transpose(matrix)
    return glMultMatrixf(matrix)

#Callback para configurar desenho na tela
def drawSetup():
    vertices = [-1, -1, -1,   -1, -1,  1,   -1,  1,  1,   -1,  1, -1,
        1, -1, -1,    1, -1,  1,    1,  1,  1,    1,  1, -1,
        -1, -1, -1,   -1, -1,  1,    1, -1,  1,    1, -1, -1,
        -1,  1, -1,   -1,  1,  1,    1,  1,  1,    1,  1, -1,
        -1, -1, -1,   -1,  1, -1,    1,  1, -1,    1, -1, -1,
        -1, -1,  1,   -1,  1,  1,    1,  1,  1,    1, -1,  1]

    colors = [0, 0, 0,   0, 0, 1,   0, 1, 1,   0, 1, 0,
        1, 0, 0,   1, 0, 1,   1, 1, 1,   1, 1, 0,
        0, 0, 0,   0, 0, 1,   1, 0, 1,   1, 0, 0,
        0, 1, 0,   0, 1, 1,   1, 1, 1,   1, 1, 0,
        0, 0, 0,   0, 1, 0,   1, 1, 0,   1, 0, 0,
        0, 0, 1,   0, 1, 1,   1, 1, 1,   1, 0, 1]

    ambient_intensity = [0.8, 0.3, 0.3, 1.0]

    direction = [0.0, 45.0, -1.0, 1.0]

    intensity = [1, 0.7, 1, 1.0]

    # Definindo a matrix, se é projeção ou ortogonal
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    frustum(-1.0, 1.0, -1.0, 1.0, 0.5, 10)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    vertices = np.array(vertices, dtype=np.float32)
    colors = np.array(colors, dtype=np.float32)

    glEnableClientState(GL_VERTEX_ARRAY)
    glVertexPointer(3, GL_FLOAT, 0, vertices)

    glEnableClientState(GL_COLOR_ARRAY)
    glColorPointer(3, GL_FLOAT, 0, colors)

    glClearColor(0.5, 0.1, 0.3, 1.0)

    #Habilitar o Z-buffer
    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LEQUAL)
    glDisable(GL_CULL_FACE)
    glCullFace(GL_BACK)

    #Habilitar iluminação
    glEnable(GL_LIGHTING)

    #Definir o modelo de iluminação
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, ambient_intensity)

    #Habilitar iluminação 0
    glEnable(GL_LIGHT0)

    # Definindo posição e intensidade da luz
    glLightfv(GL_LIGHT0, GL_POSITION, direction)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, intensity)

    # Configurando o material
    glEnable(GL_COLOR_MATERIAL)
    glColorMaterial(GL_FRONT, GL_AMBIENT_AND_DIFFUSE)
    glMaterialf(GL_FRONT, GL_SHININESS, 5.0)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, [0.1, 0.1, 0.1, 1.0])

#Callback para desenhar na tela
def drawFunction():
    
    currentTime = glfw.get_time() / 2

    glPushMatrix()
    glScale(abs(np.sin(currentTime)), abs(np.sin(currentTime)), 1)
    glRotatef(np.sin(currentTime) * 45, 0, 0, 1)
    glTranslatef(np.sin(currentTime), np.cos(currentTime), 0)

    glDrawArrays(GL_QUADS, 0, 24)
    glPopMatrix()


#Cria e configura a tela
window = Window(1280, 720, "Projeto de Sistemas Gráficos - Rodrigo e Gloria", drawSetup)
window.mainLoop(drawFunction)