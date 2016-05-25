import pygame

import BasicEnemy
import utils
from GenericPlayer import PlayerActive, Objective

pygame.init()

gameWindow = pygame.display.set_mode((1000, 600))                  #Create the game window, set up
pygame.display.set_caption("Pygame Tutorial")
clock = pygame.time.Clock()

enemies = BasicEnemy.Enemy.enemies

player = PlayerActive()                                            #The player object
objv = Objective()
scoreB = utils.ScoreBoard()

FPS = 30
gameActive = True
while gameActive:                                                  #Game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameActive = False

    activeKey = pygame.key.get_pressed()                           #Events for key presses
    if activeKey[pygame.K_RIGHT]:
        player.move(1, 0)
    if activeKey[pygame.K_LEFT]:
        player.move(-1, 0)
    if activeKey[pygame.K_UP]:
        player.move(0, -1)
    if activeKey[pygame.K_DOWN]:
        player.move(0, 1)
    if activeKey[pygame.K_SPACE]:
        player.doObjective(objv)

    cur = pygame.mouse.get_pos()
    mouse = pygame.mouse.get_pressed()                             #Events for mouse presses

    gameWindow.fill(utils.white)

    if mouse[0]:                                                   #Left-Click events
        player.shoot(cur)

    #COLLISION DETECTION
    playerCollisions = pygame.sprite.spritecollide(player, enemies, False)
    for enemy in playerCollisions:                                 #Enemy-to-player collisions
        enemy.destroy()
        player.takeDamage()

    bulletCollision = pygame.sprite.groupcollide(enemies, player.bullets, False, True)
    for enemy in bulletCollision:                                  #Enemy-to-bullet collisions
        enemy.takeDamage()

    objvCollision = pygame.sprite.spritecollide(objv, player.bullets, False)
    for bullet in objvCollision:
        tempLett = objv.winMessage[len(objv.displayMessage)]
        if tempLett.upper() == bullet.name:
            objv.displayMessage += tempLett
            objv.redraw()
            bullet.destroy()
            if objv.winMessage[len(objv.displayMessage)] == " ":
                objv.displayMessage += " "

    #Spawning
    BasicEnemy.spawn()
    #Updates
    player.update(gameWindow)
    scoreB.update(gameWindow )
    enemies.update(player)
    objv.update(gameWindow)

    #Drawing
    enemies.draw(gameWindow)

    #END drawing stuff

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
quit()