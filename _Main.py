import pygame

import BasicEnemy
import utils
from GenericPlayer import PlayerActive, Objective

pygame.init()

class Tutorial_Game():
    def __init__(self):

        self.gw = pygame.display.set_mode((1000, 600))                  #Create the game window, set up
        pygame.display.set_caption("Pygame Tutorial")
        self.clock = pygame.time.Clock()

        self.enemies = BasicEnemy.Enemy.enemies

        self.player = PlayerActive()                                            #The player object
        self.objv = Objective()
        self.scoreB = utils.ScoreBoard()

        self.FPS = 30

    def gotoMenu(self):
        menu = True
        while menu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        menu = False

                print "Intro"

                pygame.display.update()
                self.clock.tick(self.FPS)

    def pause(self):
        pause = True
        while pause:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        print "game unpaused"
                        pause = False

                text = utils.getFont(size=96, style="bold").render("Paused", True, utils.black)
                textRect = text.get_rect()
                textRect.center = self.gw.get_rect().center

                self.gw.blit(text, textRect)

                pygame.display.update()
                self.clock.tick(self.FPS)

    def playGame(self):
        self.gotoMenu()

        gameActive = True
        while gameActive:                                                  #Game loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameActive = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        print "game Paused"
                        self.pause()


            activeKey = pygame.key.get_pressed()                           #Events for key presses
            if activeKey[pygame.K_RIGHT]:
                self.player.move(1, 0)
            if activeKey[pygame.K_LEFT]:
                self.player.move(-1, 0)
            if activeKey[pygame.K_UP]:
                self.player.move(0, -1)
            if activeKey[pygame.K_DOWN]:
                self.player.move(0, 1)
            if activeKey[pygame.K_SPACE]:
                self.player.doObjective(self.objv)

            cur = pygame.mouse.get_pos()
            mouse = pygame.mouse.get_pressed()                             #Events for mouse presses

            self.gw.fill(utils.white)

            if mouse[0]:                                                   #Left-Click events
                self.player.shoot(cur)

            #COLLISION DETECTION
            playerCollisions = pygame.sprite.spritecollide(self.player, self.enemies, False)
            for enemy in playerCollisions:                                 #Enemy-to-player collisions
                enemy.destroy()
                self.player.takeDamage()

            bulletCollision = pygame.sprite.groupcollide(self.enemies, self.player.bullets, False, True)
            for enemy in bulletCollision:                                  #Enemy-to-bullet collisions
                enemy.takeDamage()

            objvCollision = pygame.sprite.spritecollide(self.objv, self.player.bullets, False)
            for bullet in objvCollision:
                tempLett = self.objv.winMessage[len(self.objv.displayMessage)]
                if tempLett.upper() == bullet.name:
                    self.objv.displayMessage += tempLett
                    self.objv.redraw()
                    bullet.destroy()
                    if self.objv.winMessage[len(self.objv.displayMessage)] == " ":
                        self.objv.displayMessage += " "

            #Spawning
            BasicEnemy.spawn()
            #Updates
            self.player.update(self.gw)
            self.scoreB.update(self.gw)
            self.enemies.update(self.player)
            self.objv.update(self.gw)

            #Drawing
            self.enemies.draw(self.gw)

            #END drawing stuff

            pygame.display.update()
            self.clock.tick(self.FPS)

        pygame.quit()
        quit()

game = Tutorial_Game()
game.playGame()