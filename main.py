import pygame, sys
from Player import Player
clock = pygame.time.Clock()

from pygame.locals import *
pygame.init()

pygame.display.set_caption('caption goes brrrr')#set caption of window
player_image = pygame.image.load('./assets/player/Idle (1).png')

moving_right = False
moving_left = False

while True:#run loop of game

    player = Player(player_image)
    player.bouncing()
    if moving_right:
        print('player move to right')
        player.move_right()
    if moving_left:
        print('player move to left')
        player.move_left()

    # handle event
    for event in pygame.event.get():
        if event.type == QUIT:
            print()
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                moving_right = True
            if event.key == K_LEFT:
                moving_left = True
        if event.type == KEYUP:
            if event.key == K_RIGHT:
                moving_right = False
            if event.key == K_LEFT:
                moving_left = False

    pygame.display.update()
    clock.tick(60)