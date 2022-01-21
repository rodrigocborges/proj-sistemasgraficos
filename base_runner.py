import random
from OpenGL.GL import *
from OpenGL.GLUT import *
from draw_morrinho import DrawMorrinho
from draw_symbol import DrawSymbol

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

    # Enable light
    glEnable(GL_LIGHTING)

    # Define light model
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, ambient_intensity)

    # Enable light 0
    glEnable(GL_LIGHT0)

    # Define light direction and intensity
    glLightfv(GL_LIGHT0, GL_POSITION, direction)
    glLightfv(GL_LIGHT0, GL_SPECULAR, intensity)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, intensity)

    # Config material
    glEnable(GL_COLOR_MATERIAL)
    glColorMaterial(GL_FRONT, GL_AMBIENT_AND_DIFFUSE)
    glMaterialf(GL_FRONT, GL_SHININESS, 5.0)
    glMaterialfv(GL_FRONT, GL_SPECULAR, [0, 0, 0, 1.0])
    glMaterialfv(GL_FRONT, GL_DIFFUSE, [0.1, 0.1, 0.1, 1.0])


def display():
    # Clear the color and depth buffers
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    # Enable z-buffer
    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LEQUAL)
    glDisable(GL_CULL_FACE)
    glCullFace(GL_BACK)

    glEnable(GL_FOG)
    glPushMatrix()
    glScalef(0.15, 0.15, 0.15)
    angle = random.choice([0, 20, 30, 50, 60])

    global time_control

    if time_control < 5 or time_control > 15:
        glDisable(GL_LIGHTING)
        DrawSymbol()
    else:
        glRotate(angle, 0, 1, 0)
        lights()
        DrawMorrinho()

    glPopMatrix()

    glutSwapBuffers()


glutInit(sys.argv)

# Create a double-buffer RGBA window
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)

# Create a window, setting its title
glutInitWindowSize(800, 500)
glutCreateWindow('FURG - Rodrigo e Gloria')

# Set the display callback
glutDisplayFunc(display)

glutTimerFunc(10, create_scene, 0)

# Run the GLUT main loop until the user closes the window
glutMainLoop()
