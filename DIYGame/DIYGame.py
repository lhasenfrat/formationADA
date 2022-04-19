from operator import truediv
import pygame,thorpy

pygame.init()


#le décor 
background = pygame.image.load("Assets/tilesetsADA/4_catacombes.png")


#paramètre la fenêtre
win_size_x=background.get_width()
win_size_y=background.get_height()
win = pygame.display.set_mode((win_size_x, win_size_y))
pygame.display.set_caption("Squarey")


#toutes les variables qui gèrent le personnage
##########################################################################
personnage = pygame.image.load("Assets/assetsADA/isaac/isaac.png")


base_personnage_x=100
base_personnage_y=100
personnage_x=base_personnage_x
personnage_y=base_personnage_y
personnage_size=[personnage.get_width()/2, personnage.get_height()/2]
personnage_vitesse=6

personnage = pygame.transform.scale(personnage, (personnage_size[0], personnage_size[1]))
##########################################################################


#toutes les variables qui gèrent l'ennemi
##########################################################################
mechant = pygame.image.load("monstro.png")

base_mechant_x=300
base_mechant_y=300
mechant_x=base_mechant_x
mechant_y=base_mechant_y
mechant_size=[mechant.get_width()/2, mechant.get_height()/2]
mechant_vitesse=3

mechant = pygame.transform.scale(mechant, (mechant_size[0], mechant_size[1]))
##########################################################################

#toutes les variables qui gèrent la porte
##########################################################################
porte_ouverte = False
porte = pygame.image.load("Assets/assetsADA/portes/porte_grille_fermee.png")

base_porte_x=430
base_porte_y=10
porte_x=base_porte_x
porte_y=base_porte_y
porte_size=[porte.get_width(), porte.get_height()]

porte = pygame.transform.scale(porte, (porte_size[0], porte_size[1]))
##########################################################################


#toutes les variables qui gèrent la clé
##########################################################################
cle_obtenue = False
cle = pygame.image.load("Assets/assetsADA/key.png")

base_cle_x=500
base_cle_y=500
cle_x=base_cle_x
cle_y=base_cle_y
cle_size=[cle.get_width()/2, cle.get_height()/2]

cle = pygame.transform.scale(cle, (cle_size[0], cle_size[1]))
##########################################################################


#toutes les fonctions de collisions 
##########################################################################
#renvoie True si le personnage touche l'ennemi (alors le jeu doit s'arrêter)
def collision_personnage_ennemi() -> bool:
    if not(personnage_x + personnage_size[0] < mechant_x or mechant_x + mechant_size[0] < personnage_x
            or personnage_y + personnage_size[1] < mechant_y or mechant_y + mechant_size[1] < personnage_y):
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
        porte = porte = pygame.image.load("Assets/assetsADA/portes/porte_grille_ouverte.png")
        porte = pygame.transform.scale(porte, (porte_size[0], porte_size[1]))


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
    mechant_x=base_mechant_x
    mechant_y=base_mechant_y
    porte_x=base_porte_x
    porte_y=base_porte_y
    cle_x=base_cle_x
    cle_y=base_cle_y
    cle_obtenue=False
    porte_ouverte = False
    porte = pygame.image.load("Assets/assetsADA/portes/porte_grille_fermee.png")

#met à jour la position du personnage
def update_personnage():
    global personnage_x, personnage_y
    keys = pygame.key.get_pressed() #liste des inputs
    if keys[pygame.K_LEFT]:
        personnage_x -= personnage_vitesse

    if keys[pygame.K_RIGHT]:
        personnage_x += personnage_vitesse

    if keys[pygame.K_UP]:
        personnage_y -= personnage_vitesse

    if keys[pygame.K_DOWN]:
        personnage_y += personnage_vitesse


#met à jour la position de l'ennemi
def update_mechant():
    global mechant_x, mechant_y
    if mechant_x < personnage_x - 10:
        mechant_x = mechant_x + mechant_vitesse
    elif mechant_x > personnage_x + 10:
        mechant_x = mechant_x - mechant_vitesse
    elif mechant_y < personnage_y - 10:
        mechant_y = mechant_y + mechant_vitesse
    elif mechant_y > personnage_y + 10:
        mechant_y = mechant_y - mechant_vitesse


#met à jour la fenêtre de jeu
def drawGame():
    update_personnage()
    update_mechant()

    #on affiche tous les éléments (personnage, méchant, arrière-plan, cle, ect...)
    win.blit(background, (0,0))
    win.blit(personnage, (personnage_x, personnage_y))
    win.blit(mechant, (mechant_x, mechant_y))
    win.blit(porte, (porte_x, porte_y))

    if not(cle_obtenue):
        win.blit(cle, (cle_x, cle_y))

    #on met à jour la fenêtre
    pygame.display.update()
    return 0

#Affichage des menus
##########################################################################
def restart():
    e_quit = thorpy.make_button("Quitter",func=thorpy.functions.quit_menu_func)
    e_restart = thorpy.make_button("Recommencer", func=play)
    e_text = thorpy.make_text("Vous êtes mort :(((((",22,(255,255,255))
    e_background = thorpy.Background( color=(0, 0, 0),elements=[e_text,e_quit,e_restart])
    thorpy.store(e_background, gap=20) 
    reload_positions()
    thorpy.functions.quit_menu_func() #Quitte le menu
    menu = thorpy.Menu(e_background) #Crée et lance le menu
    menu.play()

def win_screen():
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


application = thorpy.Application(size=(win_size_x, win_size_y), caption="Guess the number")
init()
application.quit()


pygame.quit()

