import pygame

pygame . init()
screen_width = 500
screen_height = 500
display_surface = pygame . display . set_mode ((screen_width , screen_height ))
done = True
display_surface . fill ((255,255,255))

navy = (0,0,128)
pygame . draw . circle (display_surface , navy , (250,250) ,50)
pygame . draw . circle (display_surface , navy , (100,250) ,50,3)

pygame . display . update()


while done :
    for event in pygame . event . get () :
        if event . type == pygame . QUIT :
            done = False

pygame . quit ()
