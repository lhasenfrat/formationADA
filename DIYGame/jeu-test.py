from operator import truediv
from typing import Tuple
import pygame

pygame.init()

win = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption("Squarey")

run = True


class GameObject:
    def __init__(self, posx: float, posy: float, size: Tuple[int]):
        self.x = posx
        self.y = posy  # (x,y) position en bas à gauche
        self.size = size  # size[0] = largeur et size[1]= hauteur

    def collision(self, other: "GameObject") -> bool:
        if not(self.x + self.size[0] < other.x or other.x + other.size[0] < self.x
               or self.y + self.size[1] < other.y or other.y + other.size[1] < self.y):
            return True
        else:
            return False
    
    def update(self, game):
        pass

    def draw(self, win):
        pygame.draw.rect(win, (0, 0, 255), (self.x, self.y, self.size[0], self.size[1]))

    
class Entity(GameObject):
    def __init__(self, hp:int, posx: float, posy: float, size: Tuple[int]):
        super().__init__(posx, posy, size)
        self.hp = hp
    
class Player(Entity):
    def __init__(self, hp:int, posx: float, posy: float, size: Tuple[int]):
        super().__init__(hp, posx, posy, size)
        self.vel = 5
    
    def update(self, game):
        keys = game.input #liste des inputs

        if keys[pygame.K_LEFT]:
            self.x -= self.vel

        if keys[pygame.K_RIGHT]:
            self.x += self.vel

        if keys[pygame.K_UP]:
            self.y -= self.vel

        if keys[pygame.K_DOWN]:
            self.y += self.vel

class Baddy(Entity):
    def __init__(self, hp:int, posx: float, posy: float, size: Tuple[int]):
        super().__init__(hp, posx, posy, size)
        self.vel = 4
    
    def update(self, game):
        isaac = game.player
        if self.x < isaac.x - 10:
            self.x = self.x + self.vel
        elif self.x > isaac.x + 10:
            self.x = self.x - self.vel
        elif self.y < isaac.y - 10:
            self.y = self.y + self.vel
        elif self.y > isaac.y + 10:
            self.y = self.y - self.vel


class Game:
    def __init__(self, player: Player):
        self.input=[]
        self.player = player


isaac = Player(4, 100, 100, (20,20))
baddy = Baddy(3, 200, 200, (30, 30))
game = Game(isaac)
compteur = 0 

def drawGame():
    win.fill((0, 0, 0))
    isaac.draw(win)
    baddy.draw(win)
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

    game.input=pygame.key.get_pressed()
    isaac.update(game)
    baddy.update(game)

    if isaac.collision(baddy):
        run = False

pygame.quit()


