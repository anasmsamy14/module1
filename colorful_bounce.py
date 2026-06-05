import pygame
import random


pygame.init()

sprite_color_change_event = pygame.USEREVENT + 1
background_color_change_event = pygame.USEREVENT + 2


blue = (0,0,255)
light_blue = pygame.Color('lightblue')
dark_blue = pygame.Color('darkblue')

Yellow = (255,255,0)
pink = (255,192,203)
red = (255,0,0)
white = (255,255,255)

class Sprite (pygame.sprite.Sprite):
    def __init__(self,color,height,width):
        super().__init__()
        self.image = pygame.surface([height,width])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.velocity= [random.choice([-1,1]),random.choice([-1,1])]
    def update(self):
        self.rect.move_ip(self.velocity)
        boundary_hit = False

        if self.rect.left <= 0 or self.rect.right >= 500:
            self.velocity[0] = -self.velocity[0]
            boundary_hit = True
        
        if self.rect.top <= 0 or self.rect.bottom >= 500:
            self.velocity[1] = -self.velocity[1]
            boundary_hit = True
        
        if boundary_hit:
            pygame.event.post(pygame.event.Event(sprite_color_change_event))

            pygame.event.post(pygame.event.Event(background_color_change_event))\
        
    def change_color(self):
        self.image.fill(random.choice([Yellow, pink, red, white]))

def change_background_color():
    global bg_color
    bg_color = random.choice([light_blue,blue,dark_blue])






    


