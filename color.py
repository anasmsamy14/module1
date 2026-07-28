import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Square Values")

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

font = pygame.font.Font(None, 30)

squares = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)

    pygame.draw.rect(screen, BLUE, (50, 100, 500, 100))

    text = font.render("Square values: " + str(squares), True, BLACK)
    screen.blit(text, (60, 140))

    pygame.display.update()

pygame.quit()