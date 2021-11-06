from OpenGL.GL import *
import OpenGL.GLUT as glut


class DrawSymbol:
    def __init__(self):
        self.draw_rectangle_right()

    def draw_sphere(self):
        glPushMatrix()
        glColor3ub(255, 255, 0)
        glTranslated(2, 0.1, 2)
        glScaled(2.4, 0.5, 1)
        glut.glutSolidSphere(1.15, 200, 200)
        glPopMatrix()
        self.draw_rectangle_down()

    def draw_rectangle_right(self):
        glPushMatrix()
        glColor3ub(255, 35, 35)
        glTranslated(0, 0, 0)
        glScaled(0.2, 2.0, 1)
        glut.glutSolidCube(1)
        glPopMatrix()
        self.draw_rectangle_left()

    def draw_rectangle_left(self):
        glColor3ub(255, 35, 35)
        glTranslated(-0.8, 0, 3)
        glScaled(0.2, 2.0, 1)
        glut.glutSolidCube(1)
        self.draw_sphere()

    def draw_rectangle_down(self):
        glColor3ub(255, 35, 35)
        glTranslated(2, -0.4, 0)
        glScaled(3.3, 0.2, 1)
        glut.glutSolidCube(1)
        self.draw_space_left()

    def draw_space_left(self):
        glColor3ub(0, 0, 0)
        glTranslated(-0.39, 2.5, 0)
        glScaled(0.14, 5.4, 1)
        glut.glutSolidCube(1)
        self.draw_space_right()

    def draw_space_right(self):
        glColor3ub(0, 0, 0)
        glTranslated(5.5, 0.1, -2)
        glScaled(1, 0.8, 1)
        glut.glutSolidCube(1)
        self.draw_space_down()

    def draw_space_down(self):
        glColor3ub(0, 0, 0)
        glTranslated(-2, -0.55, 0)
        glScaled(8, 0.12, 1)
        glut.glutSolidCube(1)
        self.draw_outside_sphere()

    def draw_outside_sphere(self):
        glColor3ub(255, 165, 0)
        glTranslated(-0.1, 2, 5)
        glScaled(1, 6, 1)
        glut.glutSolidSphere(1.15, 200, 200)
        self.draw_space_outside_down()

    def draw_space_outside_down(self):
        glColor3ub(0, 0, 0)
        glTranslated(0, -0.82, -2)
        glScaled(5, 0.2, 1)
        glut.glutSolidCube(1)
        self.draw_space_outside_left()

    def draw_space_outside_left(self):
        glColor3ub(0, 0, 0)
        glTranslated(-0.155, 4, 0)
        glScaled(0.04, 10, 1)
        glut.glutSolidCube(1)
        self.draw_space_outside_right()

    def draw_space_outside_right(self):
        glColor3ub(0, 0, 0)
        glTranslated(7.8, 0, 0)
        glut.glutSolidCube(1)
