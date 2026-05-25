import pygame

pygame . init()
screen_width = 500
screen_height = 500
display_surface = pygame . display . set_mode ((screen_width , screen_height ))
done = False
display_surface . fill ((0,255,0))
while not done :
    for event in pygame . event . get():
        if event . type == pygame . QUIT :
            done = True
    
    pygame.draw.rect (display_surface , (255 , 255 , 255 ),pygame.Rect(250,250,60,60))
    
    pygame.display . flip ()