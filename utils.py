import pygame
pygame.init()

#Colors
black = (0, 0, 0)
gray = (120, 120, 120)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

def getFont(name = "Courier New", size = 20, style = ''):           #POST: Returns the font the Caller wants
    return pygame.font.SysFont(name, size, style)


class ScoreBoard():

    enemiesKilled = 0
    playerAmmo = 0
    playerLives = 0

    def __init__(self):

        self.image = pygame.Surface((200, 150))
        self.image.fill(white)
        self.rect = self.image.get_rect()
        self.rect.x = 800
        self.rect.y = 0

    def drawEnemiesKilled(self):

        text = getFont(size=24, style="bold").render(("Killed: " + str(ScoreBoard.enemiesKilled)), True, black)
        self.image.blit(text, (5, 10))

    def drawPlayerAmmo(self):

        text = getFont(size=24, style="bold").render(("Ammo: " + str(ScoreBoard.playerAmmo)), True, black)
        self.image.blit(text, (5, 35))

    def drawPlayerLives(self):

        text = getFont(size=24, style="bold").render(("Lives: " + str(ScoreBoard.playerLives)), True, black)
        self.image.blit(text, (5, 60))

    def update(self, gw):
        self.image.fill(white)

        self.drawEnemiesKilled()
        self.drawPlayerAmmo()
        self.drawPlayerLives()

        gw.blit(self.image, self.rect)