import pygame

class Player:
    WINDOW_SIZE = (500, 500)
    player_location = [50, 50]
    player_y_momentum = 0
    screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)

    def __init__(self, player_image):
        self.player_image = player_image
        self.screen.fill((0, 0, 0))#set background color of game
        self.screen.blit(self.player_image, self.player_location)

    def move_right(self):
        self.player_location[0] += 1
    
    def move_left(self):
        self.player_location[0] -= 1
    
    def bouncing(self):
        if self.player_location[1] > self.WINDOW_SIZE[1]-self.player_image.get_height():
            self.player_momentum = -self.player_y_momentum
            pass
        else:
            self.player_y_momentum += 0.2
        self.player_location[1] += self.player_y_momentum