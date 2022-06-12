import pygame as pg
from pygame import surface
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

import random

import math


# nl     #no. de linhas da matriz
# nc     #no. de colunas da matriz
# pv       #porcentagem de celulas iniciais vivas

sizeX = 1200
sizeY = 1000

valColDefault = 40
valLinDefault = 50
valPVDefault = 30
nc = 1
nl = 1
pv = 1

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 170)
GREEN = (0, 170, 0)
RED = (255, 0, 0)
CYAN = (0,255,255)
MAGENTA = (255,255,0)

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

class CCelula:
    def __init__(self, est):
        self.estado = est

        #cor = random.randint(1,4)
        #if cor == 1:
            #self.vetCor = WHITE
        #elif cor == 2:
            #self.vetCor = GREEN
        #elif cor == 3:
            #self.vetCor = RED
        #else:
            #self.vetCor = BLUE
        

    def retEstado(self):
        ret = self.estado    
        return ret


class CMundo:
    def __init__(self, nnc, nnl, ppv):
        self.nc = nnc
        self.nl = nnl
        self.pv = ppv

        self.ncel = nnc*nnl

        self.listaCel = []
        self.listaProxCel = []

        random.seed()

        for i in range(0,self.ncel):
            estaViva = False
            al = random.randint(0,100)
            if (al<=self.pv):
                estaViva = True
            self.listaCel.append(CCelula(estaViva))

    def imprimeCelulas(self):
        cont = 0
        st = ""
        for i in range(self.nl):
            st += "\n"
            for j in range(self.nc):
                st += " "
                if (self.listaCel[cont].retEstado() == True):
                    st += "V"
                else:
                    st += "M"
                cont += 1

        print(st)

    def retVizinhosVivos(self,ind):
        i=ind%self.nc
        j=int(ind/self.nc)

        nVV = 0

        #vizinho 0:
        iV=i-1
        jV=j-1
        if(iV<0):
            iV = self.nc - 1
        if (jV<0):
            jV = self.nl-1
        nInd = jV*self.nc + iV

        if (self.listaCel[nInd].retEstado() == True):
            nVV += 1
        
        #vizinho 1:
        iV=i
        jV=j-1
        if (jV<0):
            jV = self.nl-1
        
        nInd = jV*self.nc + iV
        if (self.listaCel[nInd].retEstado() == True):
            nVV += 1
        
        #vizinho 2:
        iV=i+1
        if(iV==self.nc):
            iV = 0
        jV=j-1
        if (jV<0):
            jV = self.nl-1
        
        nInd = jV*self.nc + iV
        if (self.listaCel[nInd].retEstado() == True):
            nVV += 1
        
        #vizinho 3:
        iV=i-1
        if(iV<0):
            iV = self.nc-1
        jV=j
        nInd = jV*self.nc + iV

        if (self.listaCel[nInd].retEstado() == True):
            nVV += 1
        
        #vizinho 4:
        iV=i+1
        if(iV==self.nc):
            iV = 0
        jV=j
        
        nInd = jV*self.nc + iV
        if (self.listaCel[nInd].retEstado() == True):
            nVV += 1

        #vizinho 5:
        iV=i-1
        if(iV<0):
            iV = self.nc-1
        jV=j+1
        if (jV == self.nl):
            jV = 0
        nInd = jV*self.nc + iV

        if (self.listaCel[nInd].retEstado() == True):
            nVV += 1
        
        #vizinho 6:
        iV=i
        jV=j+1
        if (jV == self.nl):
            jV = 0
        
        nInd = jV*self.nc + iV

        if (self.listaCel[nInd].retEstado() == True):
            nVV += 1

        #vizinho 7:
        iV=i+1
        if(iV==self.nc):
            iV = 0
        jV=j+1
        if (jV == self.nl):
            jV = 0
        nInd = jV*self.nc + iV

        if (self.listaCel[nInd].retEstado() == True):
            nVV += 1
        
        return nVV

    def atualizaMundo(self, sc):

        self.displayMundo(sc)

        self.listaProxCel = []

        for c in range(len(self.listaCel)):
            nV = self.retVizinhosVivos(c)

            if (self.listaCel[c].retEstado() == True):
                if ((nV < 2) or (nV > 3)):
                    self.listaProxCel.append(CCelula(False))
                if (  (nV == 2) or (nV == 3)):
                    self.listaProxCel.append(CCelula(True))
            
            if (self.listaCel[c].retEstado() == False):
                if (nV == 3):
                    self.listaProxCel.append(CCelula(True))
                else:
                    self.listaProxCel.append(CCelula(False))

        for c in range(len(self.listaProxCel)):
            self.listaCel[c] = self.listaProxCel[c]


                
    def displayMundo(self, sc):
        sc.fill(BLACK)

        global sizeX
        global sizeY
        global WHITE

        arestaX = int(sizeX/self.nc)
        arestaY = int(sizeY/self.nl)

        if (arestaX < arestaY):
            aresta = arestaX
        else:
            aresta = arestaY

        ladox = aresta*self.nc
        ladoy = aresta*self.nl
        posicaox = (sizeX - ladox)/2
        posicaoy = (sizeY - ladoy)/2

        
        pg.draw.rect(sc,BLACK,[posicaox,posicaoy,ladox,ladoy],1)
        
        for c in range(len(self.listaCel)):
            i = c%self.nc
            j = int(c/self.nc)
            indicecor = self.retVizinhosVivos(c)
            if indicecor < 2:
                cor = MAGENTA
            elif (indicecor == 2) or (indicecor==3):
                cor = RED
            elif (indicecor>3):
                cor = CYAN

            posX = posicaox + aresta*i
            posY = posicaoy + aresta*j
            
            if (self.listaCel[c].retEstado() == True):
                pg.draw.rect(sc,cor,[posX,posY,aresta,aresta])
                pg.draw.rect(sc,BLACK,[posX,posY,aresta,aresta],1) 
            else:
                pg.draw.rect(sc,BLACK,[posX,posY,aresta,aresta],0)
                
def inputParamIniciais():
    global nc
    global nl
    global pv

    print("no. de colunas: (0 ->  default = " + str(valColDefault) +" )" )
    cc = input("")
    nc = valColDefault
    if (cc != ""):
        nc = int(cc)
        if (nc<0):
            nc=-nc
        else:
            if (nc==0):
                nc = valColDefault
    
    print("no. de linhas: (0 ->  default = " + str(valLinDefault) +" )" )
    cc = input("")
    nl = valLinDefault
    if (cc != ""):
        nl = int(cc)
        if (nl<0):
            nl=-nl
        else:
            if (nl==0):
                nl = valLinDefault

    print("probabilidade de celula viva inicial: (0 ->  default = " + str(valPVDefault) +" )" )
    cc = input("")
    pv = valPVDefault
    if (cc != ""):
        pv = int(cc)
        if (pv<0):
            pv=-pv
        else:
            if (pv==0):
                pv = valPVDefault

    



def main():
    pg.init()
    size = (sizeX, sizeY)
    screen = pg.display.set_mode(size)
 
#    pg.display.set_caption("Jogo da Vida - by Rodrigo Cardoso")

    inputParamIniciais()
    mundo01 = CMundo(nc,nl,pv)
    #mundo01.imprimeCelulas()
    
    screen = pg.display.set_mode(size)
    pausado = True
    avanca = False

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
                if event.key == pg.K_RETURN:
                    mundo01 = CMundo(nc,nl,pv)

                if event.key == pg.K_RIGHT:
                    if (pausado == False):
                        pausado = True
                    avanca = True

                if event.key == pg.K_ESCAPE:
                    pg.quit()
                    quit()

# 
#  
        pg.display.set_caption("Jogo da Vida")
        screen.fill(WHITE)

        #pg.draw.line(screen, GREEN, [d, c], [c, d], 1)

        #pg.draw.rect(screen, WHITE, [20, 20, 250, 100],3)

        #pg.display.flip()
        #pg.time.wait(10)

    
        if (pausado == False):
            mundo01.atualizaMundo(screen)
            pg.display.flip()

        if ((pausado == True) and (avanca == True)):
            mundo01.atualizaMundo(screen)
            pg.display.flip()
            avanca = False



if __name__ == "__main__":
    main()
