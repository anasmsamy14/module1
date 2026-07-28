import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("My First Game Screen")

image = pygame.image.load("images (1).jfif")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))
    screen.blit(image, (250, 150))

    pygame.display.update()
     

pygame.quit()