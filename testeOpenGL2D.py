import pygame as pg
from pygame import math
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

import math


def main():
    pg.init()
    display = (500, 500)
    pg.display.set_mode(display, DOUBLEBUF|OPENGL)

    ang = 1.0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
            
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                    quit()

        
        glLoadIdentity()
        
        glMatrixMode(GL_PROJECTION)
        glOrtho(0.0, 100.0, 0.0, 100.0, -10.0, 10.0)

        glClear(GL_COLOR_BUFFER_BIT)
        
        

        ang += 0.0001

        glPushMatrix()

        glTranslatef(50.0, 50.0, 0.0)
        glRotatef(360*ang/6.28, 0.0, 0.0, 1.0)

        glBegin(GL_LINES)
        glColor3f(1.0, 0.0, 0.0)
        glVertex2f(25.0, 25.0)
        glVertex2f(0.0, 0.0)
        glEnd()

        glBegin(GL_LINES)
        glColor3f(0.0,1.0,0.0)
        glVertex2f(-25.0, -25.0)
        glVertex2f(0.0, 0.0)
        glEnd()


        glBegin(GL_LINES)
        glColor3f(0.5,0.4,0.8)
        glVertex2f(0.0, 0.0)
        glVertex2f(20*math.cos(ang), 20.0*math.sin(ang))
        glEnd()

        
        if (ang > 6.28):
            ang = 0.0
       

        glPopMatrix()

        
        pg.display.flip()
        #pg.time.wait(10)

if __name__ == "__main__":
    main()