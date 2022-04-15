import pygame,thorpy

pygame.init()

#paramètre la fenêtre
win_size_x=1000
win_size_y=500 
win = pygame.display.set_mode((win_size_x, win_size_y))
pygame.display.set_caption("Squarey")

#le décor 
background = pygame.image.load("background.jpg")


#toutes les variables qui gèrent le personnage
##########################################################################
personnage = pygame.image.load("isaac.png") #on charge une image associée à notre personnage


base_personnage_x=100
base_personnage_y=100
personnage_x=base_personnage_x
personnage_y=base_personnage_y
personnage_size=[personnage.get_width()/4, personnage.get_height()/4]
personnage_vitesse=6

personnage = pygame.transform.scale(personnage, (personnage_size[0], personnage_size[1]))
##########################################################################


#toutes les variables qui gèrent la porte
##########################################################################
porte_ouverte = False
porte = pygame.image.load("porte_fermee.png")

base_porte_x=700
base_porte_y=100
porte_x=base_porte_x
porte_y=base_porte_y
porte_size=[porte.get_width()/2, porte.get_height()/2]

porte = pygame.transform.scale(porte, (porte_size[0], porte_size[1]))
##########################################################################


#toutes les variables qui gèrent la clé
##########################################################################

##########################################################################

#toutes les variables qui gèrent l'ennemi
##########################################################################

##########################################################################

#toutes les fonctions de collisions 
##########################################################################
#renvoie True si le personnage touche l'ennemi (alors le jeu doit s'arrêter)
def collision_personnage_ennemi():
    pass #à remplacer par votre code


#Si le personnage touche la cle, la variable cle_obtenue passe à True et la porte s'ouvre
def collision_personnage_cle():
    pass #à remplacer par votre code



#Si le personnage touche la porte, on a gagné et la partie s'arrête
def collision_personnage_porte():
    if porte_ouverte and not(personnage_x + personnage_size[0] < porte_x or porte_x + porte_size[0] < personnage_x
            or personnage_y + personnage_size[1] < porte_y or porte_y + porte_size[1] < personnage_y):
        return True
    return False

##########################################################################
#remet les variables dynamiques à leurs états d'origine quand on appuie sur Recommencer
def reload_positions():
    global personnage_x,personnage_y,mechant_x,mechant_y,porte_x,porte_y, cle_x,cle_y,cle_obtenue, porte_ouverte, porte
    personnage_x=base_personnage_x
    personnage_y=base_personnage_y

    porte_x=base_porte_x
    porte_y=base_porte_y

    cle_obtenue = False
    porte_ouverte = False
    porte = pygame.image.load("porte_fermee.png")
    porte = pygame.transform.scale(porte, (porte_size[0], porte_size[1]))
 

#met à jour la position du personnage
def update_personnage():
    global personnage_x, personnage_y
    keys = pygame.key.get_pressed() #liste des inputs
    if keys[pygame.K_LEFT]:
        personnage_x -= personnage_vitesse
        #insérer votre code pour que le personnage ne sorte pas de l'arène

    if keys[pygame.K_RIGHT]:
        pass #à remplacer par votre code
        #insérer votre code pour que le personnage ne sorte pas de l'arène

    if keys[pygame.K_UP]:
        pass #à remplacer par votre code
        #insérer votre code pour que le personnage ne sorte pas de l'arène

    if keys[pygame.K_DOWN]:
        pass #à remplacer par votre code
        #insérer votre code pour que le personnage ne sorte pas de l'arène

#met à jour la position de l'ennemi
def update_mechant():
    pass #à remplacer par votre code


#met à jour la fenêtre de jeu
def drawGame():
    update_personnage()
    update_mechant()

    #on affiche tous les éléments (personnage, méchant, arrière-plan, cle, ect...)
    win.blit(background, (0,0))
    win.blit(personnage, (personnage_x, personnage_y))
    #win.blit(mechant, (mechant_x, mechant_y))
    win.blit(porte, (porte_x, porte_y))

    #if not(cle_obtenue):
    #    win.blit(cle, (cle_x, cle_y))

    #on met à jour la fenêtre
    pygame.display.update()
    return 0

#Affichage des menus
##########################################################################
def ecran_restart(): # quand le personnage est mort
    pass #à remplacer par votre code


def ecran_victoire():
    e_quit = thorpy.make_button("Quitter",func=thorpy.functions.quit_menu_func)
    e_restart = thorpy.make_button("Recommencer ", func=play)
    e_text = thorpy.make_text("Vous avez gagné ! :DDDD",40,(255,255,255))
    e_background = thorpy.Background( color=(0, 0, 0),elements=[e_text,e_quit,e_restart])
    thorpy.store(e_background, gap=20) 
    reload_positions()
    thorpy.functions.quit_menu_func() #Quitte le menu
    menu = thorpy.Menu(e_background) #Crée et lance le menu
    menu.play()

def init():
    e_quit = thorpy.make_button("Quitter",func=thorpy.functions.quit_menu_func)
    e_restart = thorpy.make_button("Commencer", func=play)
    e_text = thorpy.make_text("Hello !",22,(255,255,255))
    e_background = thorpy.Background( color=(0, 0, 0),elements=[e_text,e_quit,e_restart])
    thorpy.store(e_background, gap=20) 
    menu = thorpy.Menu(e_background) #Crée et lance le menu
    menu.play()


##########################################################################


#Boucle principale qui change l'état du jeu toute les 16ms
#on fait une boucle qui met à jour la fenêtre de jeu toutes les 16ms et qui s'arrête quand on ferme la fenêtre ou quand on perd 
# (quand le personnage touche l'ennemi)
##########################################################################
def play():
    run = True
    victory=False
    while run:
        pygame.time.delay(16)

        #on met à jour la fenêtre
        drawGame()
        
        #si on ferme la fenêtre, le jeu s'arrête
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        #si jamais le personnage touche le méchant, le jeu s'arrête

    if collision_personnage_porte() :
            run=False
            victory=True
    if not victory:
        ecran_restart()
    else:
        ecran_victoire()
##########################################################################


application = thorpy.Application(size=(win_size_x, win_size_y), caption="ADA Game")
init()
application.quit()


pygame.quit()

