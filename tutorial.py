import pygame, sys
from Player import Player
clock = pygame.time.Clock()

from pygame.locals import *
pygame.init()

pygame.display.set_caption('caption goes brrrr')#set caption of window
player_image = pygame.image.load('./assets/player/Idle (1).png')
player_image = pygame.transform.scale(player_image, (80, 100))


WINDOW_SIZE = (400, 400)
player_location = [0, 0]
screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)

moving_right = False
moving_left = False
player_y_momentum = 0

player_rect = pygame.Rect(player_location[0], player_location[1], player_image.get_width(), player_image.get_height())
test_rect = pygame.Rect(100,100,100,50)

while True:#run loop of game
    screen.fill((0, 0, 0))#set background color of game
    screen.blit(player_image, player_location)

    if player_location[1] > WINDOW_SIZE[1]-player_image.get_height():
        player_y_momentum = -player_y_momentum
    else:
        player_y_momentum += 0.2

    player_location[1] += player_y_momentum
    print(player_y_momentum)
    if moving_right:
        print(player_image.get_height())
        player_location[0] += 1
    if moving_left:
        player_location[0] -= 1
        print('player move to left')

#   update player rect x and y
    player_rect.x = player_location[0]
    player_rect.y = player_location[1]

    if player_rect.colliderect(test_rect):
        print('player is collide with test rect')
        pygame.draw.rect(screen, (255, 0, 0), test_rect)#draw a rect to red
    else:
        pygame.draw.rect(screen, (0, 0, 255), test_rect)#draw a rect to blue


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