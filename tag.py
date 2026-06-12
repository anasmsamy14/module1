import pygame 
import random

screen_width , screen_height = 800, 600

movement_speed = 3
font_size = 73

pygame.init()


baground_image = pygame.trransform.scale(pygame.image.load("color.jpg"), (screen_width, screen_height))

font = pygame.font.SysFont("Arial", font_size)


class sprite(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(
            pygame.color('blue'))
        pygame.draw.rect(self.image, color, pygame.Rect(0, 0, width, height)) 
        self.rect = self.image.get_rect()
    

    def move(self, x_change, y_change):
        self.rect.x = max(
            min(self.rect.x + x_change, screen_width - self.rect.width), 0)
        
        self.rect.y = max(
            min(self.rect.y + y_change, screen_height - self.rect.height), 0)
    

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Move the square with arrow keys")
        