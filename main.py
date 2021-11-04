import glfw
from OpenGL.GL import *
import numpy as np

from window import Window

#Alguns exemplos: https://github.com/Somsubhra/pyOpenGL-Samples


#Callback para configurar desenho na tela
def drawSetup():
    vertices = [-0.5, -0.5, 0.0, 
                 0.5, -0.5, 0.0, 
                 0.0, 0.5, 0.0]

    colors = [1.0, 0.0, 0.0, 
              0.0, 1.0, 0.0, 
              0.0, 0.0, 1.0]

    ambient_intensity = [0.3, 0.3, 0.3, 1.0]

    direction = [0.0, 2.0, -1.0, 1.0]

    intensity = [0.7, 0.7, 0.7, 1.0]

    # Definindo a matrix, se é projeção ou ortogonal
    glMatrixMode(GL_PROJECTION)

    vertices = np.array(vertices, dtype=np.float32)
    colors = np.array(colors, dtype=np.float32)

    glEnableClientState(GL_VERTEX_ARRAY)
    glVertexPointer(3, GL_FLOAT, 0, vertices)

    glEnableClientState(GL_COLOR_ARRAY)
    glColorPointer(3, GL_FLOAT, 0, colors)

    glClearColor(0.5, 0.1, 0.3, 1.0)

    #Habilitar o Z-buffer
    glEnable(GL_DEPTH_TEST)

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

#Callback para desenhar na tela
def drawFunction():
    
    currentTime = glfw.get_time()

    glLoadIdentity()
    glScale(abs(np.sin(currentTime)), abs(np.sin(currentTime)), 1)
    glRotatef(np.sin(currentTime) * 45, 0, 0, 1)
    glTranslatef(np.sin(currentTime), np.cos(currentTime), 0)

    glDrawArrays(GL_TRIANGLES, 0, 3)

#Cria e configura a tela
window = Window(1280, 720, "Projeto de Sistemas Gráficos - Rodrigo e Gloria", drawSetup)
window.mainLoop(drawFunction)