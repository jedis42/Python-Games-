import time
import pygame
import Classe
import core
import random

xBall = 100
yBall = 400
speedx = 7
speedy = 6
r=255
g=0
b=0
x = 800
y = 500
rayon = 50
keys = 0
screen =0
drops = []
compt= 0

def setup():
    print("setup START----------")
    core.fps = 60
    core.WINDOW_SIZE = [x, y]
    #screen = pygame.display.set_mode(Classe.def_ecran.resolution())
    print("setup END-----------")


def run():
    global xBall, yBall, compt, r, g, b, speedx, speedy, rayon

    Monimage = Classe.Background(800,500,0,0)
    Monimage.image()

    #icon = pygame.image.load("Earth_Moon_547876_3840x2160.jpg")
    #icon.convert()
    #icon = pygame.transform.scale(icon, (700, 500))
    #core.screen.blit(icon, (0, 0))


    pygame.draw.rect(core.screen, (r, g, b),(0, 450,800,50))
    icon = pygame.image.load("astronaut.png")
    icon.convert_alpha()
    icon = pygame.transform.scale(icon,(rayon, rayon))
    core.screen.blit(icon, (xBall, yBall))


    time.sleep(0.01)


    xBall = xBall
    yBall = 400


    #if xBall >= core.WINDOW_SIZE[0] - rayon  or xBall <= 0 :
        #speedx = -speedx

        #r = random.uniform(1, 255)
        #g = random.uniform(1, 255)
        #b = random.uniform(1, 255)

    #if yBall >= core.WINDOW_SIZE[1] - rayon - 50 or yBall <= 0 :

        #speedy = -speedy

    keys = pygame.key.get_pressed()


    if keys[pygame.K_SPACE]:
        print ("vrinfvirvnirv ")
        if yBall >= 400 :
            yBall = yBall - 50

    if keys[pygame.K_RIGHT]:
        xBall = xBall +5
    if keys[pygame.K_LEFT]:
        xBall = xBall - 5





    #for event in pygame.event.get():
        #if event.type == KEYDOWN:
            #print(event.unicode)

    #if evenement.type == KEYDOWN:
        #print("Une touche est pressée")
        #listeTouche = pygame.key.get_pressed()
        #if listeTouche[K_SPACE]:
            #print("La touche espace est pressée.")
        #if listeTouche[K_UP]:
            #print("La flèche vers le haut est pressée.")

    r = random.uniform(1, 255)
    g = random.uniform(1, 255)
    b = random.uniform(1, 255)










core.main(setup, run)