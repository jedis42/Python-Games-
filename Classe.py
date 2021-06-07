import pygame

import core


class personnage :
    xPosition = 0
    yPosition = 0
    HP = 1
    Image =0
    xTaille = 0
    yTaille = 0
    def GetxPosition(self):
        return xPosition

    def __init__(self, x, y):
        self.xTaille = xT
        self.yTaille = yT
        self.xPosition = xP
        self.yPosition = yP


class Background:
    Image = 0
    xPosition = 0
    yPosition = 0
    xTaille = 0
    yTaille = 0

    def __init__(self,a,b,c,d):
        self.xTaille =a
        self.yTaille =b
        self.yPosition =c
        self.xPosition =d
    def image(self):
        Image = pygame.image.load("Earth_Moon_547876_3840x2160.jpg")
        Image.convert
        Image = pygame.transform.scale(Image, (self.xTaille, self.yTaille))
        core.screen.blit(Image,(self.xPosition,self.yPosition))


#class ecran (object) :
    #def __init__(self,largeur,hauteur):
        #self.largeur = largeur
        #self.hauteur = hauteur

    #def resolution (self):
        #return (self.largeur, self.hauteur)

    #def printecran (self):
        #print ("hauteur" +str(self.hauteur))
       # print ("largeur" +str(self.largeur))
        #print ("resolution" +str(self.resolution()))

#def_ecran = ecran(1000,1200)









