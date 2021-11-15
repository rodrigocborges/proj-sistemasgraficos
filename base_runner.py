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
    glutTimerFunc(2000, create_scene, 0)
    glutPostRedisplay()

def display():
    # Clear the color and depth buffers
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_FOG)
    glPushMatrix()
    glScalef(0.15, 0.15, 0.15)
    angle = random.choice([0, 20, 30, 50, 60])
    position_x = random.randint(0, 5)
    position_y = random.randint(0, 5)
    global time_control
    if time_control < 5 or time_control > 15:
        DrawSymbol()
    else:
        print(angle)
        glRotate(angle, 0, 1, 0)
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
glutCreateWindow('FURG - Rodrigo e Gloria')

# Set the display callback.  You can set other callbacks for keyboard and
# mouse events.
glutDisplayFunc(display)

glutTimerFunc(10, create_scene, 0)

# Run the GLUT main loop until the user closes the window.
glutMainLoop()