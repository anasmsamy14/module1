import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))

WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)

    pygame.draw.rect(screen, YELLOW, (250, 250, 300, 100))

    text = pygame.font.Font(None, 50).render("Hi I'm coding", True, BLACK)
    screen.blit(text, (250, 180))

    pygame.display.update()

pygame.quit()