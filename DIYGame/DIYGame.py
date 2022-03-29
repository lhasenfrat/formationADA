from operator import truediv
from typing import Tuple
import pygame

pygame.init()

win = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption("Squarey")

run = True

def collision() -> bool:
    if not(isaac_x + isaac_size[0] < baddy_x or baddy_x + baddy_size[0] < isaac_x
            or isaac_y + isaac_size[1] < baddy_y or baddy_y + baddy_size[1] < isaac_y):
        return True
    else:
        return False
    
def update_isaac():
    global isaac_x, isaac_y
    keys = pygame.key.get_pressed() #liste des inputs
    if keys[pygame.K_LEFT]:
        isaac_x -= isaac_velocite

    if keys[pygame.K_RIGHT]:
        isaac_x += isaac_velocite
        #faire aller le personnage à droite

    if keys[pygame.K_UP]:
        isaac_y -= isaac_velocite

    if keys[pygame.K_DOWN]:
        isaac_y += isaac_velocite

def draw():
    pygame.draw.rect(win, (0, 0, 255), (isaac_x, isaac_y, isaac_size[0], isaac_size[1]))
    pygame.draw.rect(win, (0, 0, 255), (baddy_x, baddy_y, baddy_size[0], baddy_size[1]))

def update_baddy():
    global baddy_x, baddy_y
    if baddy_x < isaac_x - 10:
        baddy_x = baddy_x + baddy_velocite
    elif baddy_x > isaac_x + 10:
        baddy_x = baddy_x - baddy_velocite
    elif baddy_y < isaac_y - 10:
        baddy_y = baddy_y + baddy_velocite
    elif baddy_y > isaac_y + 10:
        baddy_y = baddy_y - baddy_velocite
        
isaac_x=100
isaac_y=100
isaac_size=[20,20]
isaac_velocite=4

baddy_x=300
baddy_y=300
baddy_size=[30,30]
baddy_velocite=3

compteur = 0 

def drawGame():
    win.fill((0, 0, 0))
    draw()
    pygame.display.update()
    return 0

#character = pygame.image.load("isaac.png")
#win.blit(character,(50,50)) # These are the X and Y coordinates
drawGame()


while run:
    pygame.time.delay(16)

    drawGame()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    
    update_isaac()
    update_baddy()

    if collision():
        run = False

pygame.quit()

