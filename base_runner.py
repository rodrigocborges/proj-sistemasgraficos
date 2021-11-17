import random
import sys
import time

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from draw_morrinho import DrawMorrinho
from draw_symbol import DrawSymbol
import numpy as np
# The display() method does all the work; it has to call the appropriate
# OpenGL functions to actually display something.
global time_control
time_control = 0

def create_scene(time,):
    global time_control
    time_control = time_control + 1
    glutTimerFunc(1000, create_scene, 0)
    glutPostRedisplay()

def lights():
    ambient_intensity = [1, 1, 1, 1.0]

    direction = [0.0, 45.0, -1.0, 1.0]

    intensity = [1, 0.7, 1, 1.0]

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

def display():
    # Clear the color and depth buffers
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    #Habilitar o Z-buffer
    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LEQUAL)
    glDisable(GL_CULL_FACE)
    glCullFace(GL_BACK)

    glEnable(GL_FOG)
    glPushMatrix()
    glScalef(0.15, 0.15, 0.15)
    angle = random.choice([0, 20, 30, 50, 60])
    position_x = random.randint(0, 5)
    position_y = random.randint(0, 5)
    global time_control
    if time_control < 5 or time_control > 15:
        glDisable(GL_LIGHTING)
        DrawSymbol()
    else:
        print(angle)
        glRotate(angle, 0, 1, 0)
        lights()
        DrawMorrinho()

    glPopMatrix()
    # ... render stuff in here ...
    # It will go to an off-screen frame buffer.
    # Copy the off-screen buffer to the screen.
    glutSwapBuffers()

glutInit(sys.argv)

# Create a double-buffer RGBA window.   (Single-buffering is possible.
# So is creating an index-mode window.)
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)

# Create a window, setting its title
glutInitWindowSize(800, 500)
glutCreateWindow('FURG - Rodrigo e Gloria')

# Set the display callback.  You can set other callbacks for keyboard and
# mouse events.
glutDisplayFunc(display)

glutTimerFunc(10, create_scene, 0)

# Run the GLUT main loop until the user closes the window.
glutMainLoop()