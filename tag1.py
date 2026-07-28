import pygame 
import random

screen_width , screen_height = 800, 600

movement_speed = 3
font_size = 73

pygame.init()


baground_image = pygame.transform.scale(pygame.image.load("color.jpg"), (screen_width, screen_height))

font = pygame.font.SysFont("Arial", font_size)


class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(
            pygame.Color('blue'))
        pygame.draw.rect(self.image, color, pygame.Rect(0, 0, width, height)) 
        self.rect = self.image.get_rect()
    

    def move(self, x_change, y_change):
        self.rect.x = max(
            min(self.rect.x + x_change, screen_width - self.rect.width), 0)
        
        self.rect.y = max(
            min(self.rect.y + y_change, screen_height - self.rect.height), 0)
    

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Move the square with arrow keys")
all_sprites = pygame.sprite.Group()


sprite1 = Sprite(pygame.Color('black'),20,30)
sprite1.rect.x = random.randint(0, screen_width - sprite1.rect.width)
sprite1.rect.y = random.randint(0, screen_height - sprite1.rect.height)

all_sprites.add(sprite1)

sprite2 = Sprite(pygame.Color('red'),20,30)
sprite2.rect.x = random.randint(0, screen_width - sprite2.rect.width)
sprite2.rect.y = random.randint(0, screen_height - sprite2.rect.height)

all_sprites.add(sprite2)


running,won = True,False
clock = pygame.time.Clock()


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_x):
            running = False
        
    if not won:
        keys = pygame.key.get_pressed()
        x_change = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * movement_speed
        y_change = (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * movement_speed
        sprite1.move(x_change, y_change)

        if sprite1.rect.colliderect(sprite2.rect):
            sprite2.rect.x = random.randint(0, screen_width - sprite2.rect.width)
            sprite2.rect.y = random.randint(0, screen_height - sprite2.rect.height)
            won = True
            phase2_start_time = pygame.time.get_ticks()
    screen.blit(baground_image, (0, 0))
    all_sprites.draw(screen)

    if won:
        win_text = font.render('PHASE 2', True, pygame.Color("green"))
        
        screen.blit(win_text, ((screen_width - win_text.get_width()) // 2, (screen_height - win_text.get_height()) // 2))
        if pygame.time.get_ticks() - phase2_start_time > 2000:  
            won = False
    pygame.display.flip()
    clock.tick(60)

pygame.quit()