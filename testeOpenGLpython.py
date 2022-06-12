import pygame as pg
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *


cubeVertices = ((1,1,1),(1,1,-1),(1,-1,-1),(1,-1,1),(-1,1,1),(-1,-1,-1),(-1,-1,1),(-1,1,-1))
cubeEdges = ((0,1),(0,3),(0,4),(1,2),(1,7),(2,5),(2,3),(3,6),(4,6),(4,7),(5,6),(5,7))
cubeQuads = ((0,3,6,4),(2,5,6,3),(1,2,5,7),(1,0,4,7),(7,4,6,5),(2,3,0,1))

def wireCube():
    glBegin(GL_LINES)
    for cubeEdge in cubeEdges:
        for cubeVertex in cubeEdge:
            glVertex3fv(cubeVertices[cubeVertex])
    glEnd()

def solidCube():
    glBegin(GL_QUADS)
    for cubeQuad in cubeQuads:
        for cubeVertex in cubeQuad:
            glVertex3fv(cubeVertices[cubeVertex])
    glEnd()

def main():
    pg.init()
    display = (1680, 1050)
    pg.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(100, (display[0]/display[1]), 0.1, 50.0)

    

    ang = 0.0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
            
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                    quit()

        

        ang += 0.5
        if (ang>360.0):
            ang = 0.0
        glPushMatrix()
        glTranslatef(0.0, 0.0, -5)
        glRotatef(45.0, 1,1,-1)
        glRotatef(ang, 1, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        #solidCube()
        wireCube()
        glPopMatrix()

        glPushMatrix()
        glTranslatef(0.0, 5.0, -5.0)
        glRotatef(ang, 1, 1, 1)
        wireCube()
        glPopMatrix()

        pg.display.flip()
        pg.time.wait(10)

if __name__ == "__main__":
    main()