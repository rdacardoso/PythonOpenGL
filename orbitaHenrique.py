import pygame as pg
from pygame import surface
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

import math


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

def retornaStr(p1X, n):
    cont = 0
    stp1X = str(p1X)
    st1x = ""
    passeiPonto = False
    for c in stp1X:
        if c == ".":
            passeiPonto = True
        if passeiPonto == True:
            cont += 1
        if (cont <= n):
            st1x += c
    return st1x


def main():
    pg.init()
    size = (1000, 1000)
    screen = pg.display.set_mode(size)
 
    pg.display.set_caption("Jogo da Vida - by Rodrigo Cardoso")

    dx = 0.25
    x = 0
    k=5
    dk=0.5
    pausado = False
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    if (pausado == False): 
                        pausado = True
                    else:
                        pausado = False
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                    quit()
        
        if (pausado == False):
            x += dx
        screen.fill(BLACK)


        a = 500
        b = 500
        c = 400 - 100*math.sin(x/50)
        d = 400 + 100*math.cos(x/50)
    
        p1X = d
        p1Y = c
        p2X = c
        p2Y = d

        dist = math.sqrt(   (p1X-p2X)*(p1X-p2X) + (p1Y-p2Y)*(p1Y-p2Y) )
        if (dist <= k):
            if (pausado == False):
                k += dk

        pg.draw.line(screen, GREEN, [d, c], [c, d], 1)
        pg.draw.circle(screen, RED,[p1X,p1Y],k)
        pg.draw.circle(screen, WHITE,[p2X,p2Y],k)
        pg.draw.circle(screen,GREEN,[400,400], 100, 1)

        Font=pg.font.SysFont('arial',  20)
        
        st1x = retornaStr(p1X, 2)
        letter1=Font.render(st1x, False, RED, BLACK)
        screen.blit(letter1, (80, 100))
        st1y = retornaStr(p1Y, 2)
        letter2=Font.render(st1y, False, RED, BLACK)
        screen.blit(letter2, (180, 100))

        st2x = retornaStr(p2X, 2)
        letter3=Font.render(st2x, False, RED, BLACK)
        screen.blit(letter3, (380, 100))
        st2y = retornaStr(p2Y, 2)
        letter4=Font.render(st2y, False, RED, BLACK)
        screen.blit(letter4, (480, 100))

        #pg.draw.rect(screen, WHITE, [20, 20, 250, 100],3)

        pg.display.flip()
        #pg.time.wait(10)

if __name__ == "__main__":
    main()