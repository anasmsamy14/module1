import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Sprites")

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

x1 = 100
y1 = 100


x2 = 400
y2 = 300

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        y1 -= 5
    if keys[pygame.K_DOWN]:
        y1 += 5
    if keys[pygame.K_LEFT]:
        x1 -= 5
    if keys[pygame.K_RIGHT]:
        x1 += 5

    screen.fill(WHITE)

    pygame.draw.rect(screen, BLUE, (x1, y1, 50, 50))
    pygame.draw.rect(screen, RED, (x2, y2, 50, 50))

    pygame.display.update()

pygame.quit()