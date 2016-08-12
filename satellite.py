from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from planet import *

class Satellite(Planet):

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        return

    def draw(self, quadratic):

        glPushMatrix()
        glTranslatef(self.posX, self.posY, self.posZ)

        glRotatef(self.rotX, 1.0, 0.0, 0.0)            # Rotate The Cube On It's X Axis
        glRotatef(self.rotY, 0.0, 1.0, 0.0)            # Rotate The Cube On It's Y Axis
        glRotatef(self.rotZ, 0.0, 0.0, 1.0)            # Rotate The Cube On It's Z Axis

        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, self.texID)
        glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_REPLACE)
        gluSphere(quadratic, self.radius, 64, 64)
        glDisable(GL_TEXTURE_2D)
        glPopMatrix()
