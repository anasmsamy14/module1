import pygame

pygame.init()

screen = pygame.display.set_mode((600, 400))


color1 = (255, 0, 0)
color2 = (0, 0, 255)


CHANGE_COLOR = pygame.USEREVENT + 1
pygame.time.set_timer(CHANGE_COLOR, 2000)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == CHANGE_COLOR:
            color1 = (0, 255, 0)
            color2 = (255, 255, 0)

    screen.fill((255, 255, 255))

    
    pygame.draw.rect(screen, color1, (100, 150, 50, 50))
    pygame.draw.rect(screen, color2, (300, 150, 50, 50))

    pygame.display.update()

pygame.quit()