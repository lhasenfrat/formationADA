from operator import truediv
import re
from typing import Tuple
import pygame,thorpy

pygame.init()

#paramètre la fenêtre
win_size_x=1000
win_size_y=500 
win = pygame.display.set_mode((win_size_x, win_size_y))
pygame.display.set_caption("Squarey")

#le décor 
background = pygame.image.load("Assets/tilesetsADA/4_catacombes.png")


#toutes les variables qui gèrent le personnage
##########################################################################
personnage = pygame.image.load("Assets/assetsADA/isaac/isaac.png")


base_personnage_x=100
base_personnage_y=100
personnage_x=base_personnage_x
personnage_y=base_personnage_y
personnage_size=[personnage.get_width()/4, personnage.get_height()/4]
personnage_velocite=6

personnage = pygame.transform.scale(personnage, (personnage_size[0], personnage_size[1]))
##########################################################################


#toutes les variables qui gèrent l'ennemi
##########################################################################
baddy = pygame.image.load("monstro.png")

base_baddy_x=300
base_baddy_y=300
baddy_x=base_baddy_x
baddy_y=base_baddy_y
baddy_size=[baddy.get_width()/2, baddy.get_height()/2]
baddy_velocite=3

baddy = pygame.transform.scale(baddy, (baddy_size[0], baddy_size[1]))
##########################################################################

#toutes les variables qui gèrent la porte
##########################################################################
porte_ouverte = False
porte = pygame.image.load("Assets/assetsADA/portes/porte_grille_ouverte.png")

base_porte_x=700
base_porte_y=100
porte_x=base_porte_x
porte_y=base_porte_y
porte_size=[porte.get_width()/2, porte.get_height()/2]

porte = pygame.transform.scale(porte, (porte_size[0], porte_size[1]))
##########################################################################


#toutes les variables qui gèrent la clé
##########################################################################
cle_obtenue = False
cle = pygame.image.load("Assets/assetsADA/key.png")

base_cle_x=500
base_cle_y=100
cle_x=base_cle_x
cle_y=base_cle_y
cle_size=[cle.get_width()/4, cle.get_height()/4]

cle = pygame.transform.scale(cle, (cle_size[0], cle_size[1]))
##########################################################################


#toutes les fonctions de collisions 
##########################################################################
#renvoie True si le personnage touche l'ennemi (alors le jeu doit s'arrêter)
def collision_personnage_ennemi() -> bool:
    if not(personnage_x + personnage_size[0] < baddy_x or baddy_x + baddy_size[0] < personnage_x
            or personnage_y + personnage_size[1] < baddy_y or baddy_y + baddy_size[1] < personnage_y):
        return True
    else:
        return False

#Si le personnage touche la cle, la variable cle_obtenue passe à True et la porte s'ouvre
def collision_personnage_cle():
    global cle_obtenue, porte_ouverte, porte
    if not(personnage_x + personnage_size[0] < cle_x or cle_x + cle_size[0] < personnage_x
            or personnage_y + personnage_size[1] < cle_y or cle_y + cle_size[1] < personnage_y):
        cle_obtenue = True
        porte_ouverte = True

        #remplace l'image de la porte fermee par l'image de la porte ouverte
        porte = porte = pygame.image.load("DIYGame/assetsADA/portes/porte_grille_fermee.png")
        porte = pygame.transform.scale(porte, (porte_size[0], porte_size[1]))


#Si le personnage touche la porte, on a gag,é et la partie s'arrête
def collision_personnage_porte():
    global cle_obtenue, porte_ouverte, porte
    if not(personnage_x + personnage_size[0] < porte_x or porte_x + porte_size[0] < personnage_x
            or personnage_y + personnage_size[1] < porte_y or porte_y + porte_size[1] < personnage_y):
        return True
    return False

##########################################################################

#remet les variables dynamiques à leurs états d'origine
def reload_positions():
    global personnage_x,personnage_y,baddy_x,baddy_y,porte_x,porte_y, cle_x,cle_y,cle_obtenue
    personnage_x=base_personnage_x
    personnage_y=base_personnage_y
    baddy_x=base_baddy_x
    baddy_y=base_baddy_y
    porte_x=base_porte_x
    porte_y=base_porte_y
    cle_x=base_cle_x
    cle_y=base_cle_y
    cle_obtenue=False

#met à jour la position du personnage
def update_personnage():
    global personnage_x, personnage_y
    keys = pygame.key.get_pressed() #liste des inputs
    if keys[pygame.K_LEFT]:
        personnage_x -= personnage_velocite

    if keys[pygame.K_RIGHT]:
        personnage_x += personnage_velocite
        #faire aller le personnage à droite

    if keys[pygame.K_UP]:
        personnage_y -= personnage_velocite

    if keys[pygame.K_DOWN]:
        personnage_y += personnage_velocite


#met à jour la position de l'ennemi
def update_baddy():
    global baddy_x, baddy_y
    if baddy_x < personnage_x - 10:
        baddy_x = baddy_x + baddy_velocite
    elif baddy_x > personnage_x + 10:
        baddy_x = baddy_x - baddy_velocite
    elif baddy_y < personnage_y - 10:
        baddy_y = baddy_y + baddy_velocite
    elif baddy_y > personnage_y + 10:
        baddy_y = baddy_y - baddy_velocite


#met à jour la fenêtre de jeu
def drawGame():
    #on affiche tous les éléments (personnage, méchant, arrière-plan, ect...)
    win.blit(background, (0,0))
    win.blit(personnage, (personnage_x, personnage_y))
    win.blit(baddy, (baddy_x, baddy_y))
    win.blit(porte, (porte_x, porte_y))

    
    if not(cle_obtenue):
        win.blit(cle, (cle_x, cle_y))

    #on met à jour la fenêtre
    pygame.display.update()
    return 0

#Affichage des menus
##########################################################################
def restart():
    e_quit = thorpy.make_button("Quit",func=thorpy.functions.quit_menu_func)
    e_restart = thorpy.make_button("Restart", func=play)
    e_text = thorpy.make_text("You died",22,(255,0,0))
    e_background = thorpy.Background( color=(200, 200, 255),elements=[e_text,e_quit,e_restart])
    thorpy.store(e_background, gap=20) 
    reload_positions()
    thorpy.functions.quit_menu_func() #quit the current menu
    menu = thorpy.Menu(e_background) #create and launch the menu
    menu.play()

def win_screen():
    e_quit = thorpy.make_button("Quit",func=thorpy.functions.quit_menu_func)
    e_restart = thorpy.make_button("Restart", func=play)
    e_text = thorpy.make_text("You won !",40,(255,255,0))
    e_background = thorpy.Background( color=(200, 200, 255),elements=[e_text,e_quit,e_restart])
    thorpy.store(e_background, gap=20) 
    reload_positions()
    thorpy.functions.quit_menu_func() #quit the current menu
    menu = thorpy.Menu(e_background) #create and launch the menu
    menu.play()

def init():
    e_quit = thorpy.make_button("Quit",func=thorpy.functions.quit_menu_func)
    e_restart = thorpy.make_button("Start", func=play)
    e_text = thorpy.make_text("Hello",22,(0,255,0))
    e_background = thorpy.Background( color=(200, 200, 255),elements=[e_text,e_quit,e_restart])
    thorpy.store(e_background, gap=20) 
    menu = thorpy.Menu(e_background) #create and launch the menu
    menu.play()


##########################################################################

#Boucle principale qui change l'état du jeu toute les 16ms
##########################################################################
def play():
    run = True
    victory=False
    while run:
        pygame.time.delay(16)

        #on met à jour la position des éléments qui bougent, puis on met à jour la fenêtre
        update_personnage()
        update_baddy()
        drawGame()
        
        #si on ferme la fenêtre, le jeu s'arrête
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        #si jamais le personnage touche le méchant, le jeu s'arrête
        if collision_personnage_ennemi():
            run = False
        
        collision_personnage_cle()

        if cle_obtenue and collision_personnage_porte() :
            run=False
            victory=True
    if not victory:
        restart()
    else:
        win_screen()
##########################################################################


#on fait une boucle qui met à jour la fenêtre de jeu toutes les 16ms et qui s'arrête quand on ferme la fenêtre ou quand on perd 
# (quand le personnage touche l'ennemi)

application = thorpy.Application(size=(win_size_x, win_size_y), caption="Guess the number")
init()
application.quit()


pygame.quit()

