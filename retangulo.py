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

telahorizontal = 100 #int(input('tamanho horizontal'))
telavertical = 100 #int(input('tamanho vertical'))
nl = 20 #int(input('numero de linhas'))
nc = 10 #int(input('numero de colunas'))

if telahorizontal/nc >= telavertical/nl:
    menoraresta = telavertical/nl
else:
    menoraresta = telahorizontal/nc

ladox = menoraresta*nc
ladoy = menoraresta*nl
posicaox = (telahorizontal - ladox)/2
posicaoy = (telavertical - ladoy)/2


def main():
    pg.init()
    size = (telahorizontal, telavertical)
    screen = pg.display.set_mode(size)

    pg.display.set_caption("Jogo da Vida")
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
        pg.draw.rect(screen,WHITE,[posicaox,posicaoy,ladox,ladoy],1)
        pg.display.flip()
main()