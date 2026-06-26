import pygame
import random

pygame.init()

# Screen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Invaders")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Player
player = pygame.Rect(370, 500, 50, 50)

# Enemies
enemies = []
for i in range(7):
    enemy = pygame.Rect(random.randint(0, 750), random.randint(50, 250), 50, 50)
    enemies.append(enemy)

# Score
score = 0
font = pygame.font.SysFont(None, 40)

running = True
while running:

    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player.x -= 5
    if keys[pygame.K_RIGHT]:
        player.x += 5
    if keys[pygame.K_UP]:
        player.y -= 5
    if keys[pygame.K_DOWN]:
        player.y += 5

    # Keep player on screen
    if player.x < 0:
        player.x = 0
    if player.x > 750:
        player.x = 750
    if player.y < 0:
        player.y = 0
    if player.y > 550:
        player.y = 550

    # Draw player
    pygame.draw.rect(screen, BLUE, player)

    # Draw enemies and check collisions
    for enemy in enemies:
        pygame.draw.rect(screen, RED, enemy)

        if player.colliderect(enemy):
            score += 1
            enemy.x = random.randint(0, 750)
            enemy.y = random.randint(50, 250)

    # Draw score
    text = font.render("Score: " + str(score), True, BLACK)
    screen.blit(text, (10, 10))

    pygame.display.update()

pygame.quit()