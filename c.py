import pygame

def main():
    pygame . init ()
    screen_width, screen_height = 500,500
    display_surface = pygame . display . set_mode ((screen_width, screen_height))
    pygame . display . set_caption ('color changing sprite')
    display_surface . fill ((255,255,255))
    color = {'navy': (0,0,128), 'red': (255,0,0), 'green': (0,255,0), 'blue': (0,0,255), 'yellow': (255,255,0), 'cyan': (0,255,255), 'magenta': (255,0,255), 'black': (0,0,0)}

    current_color = color['navy']

    x,y = 30,30

    sprite_width, sprite_height = 50,50
    
    clock = pygame . time . Clock ()

    done = False
    while not done:
        for event in pygame . event . get ():
            if event . type == pygame . QUIT :
                done = True
        prresed = pygame . key . get_pressed ()
        if prresed [pygame . K_LEFT ]: x-= 3
        if prresed [pygame . K_RIGHT ]: x+= 3
        if prresed [pygame . K_UP ]: y-= 3  
        if prresed [pygame . K_DOWN ]: y+= 3

        x = min(max(0,x), screen_width - sprite_width)
        y = min(max(0,y), screen_height - sprite_height)
        if x == 0: current_color = color['red']
        elif x == screen_width - sprite_width: current_color = color['green']
        elif y == 0: current_color = color['blue']
        elif y == screen_height - sprite_height: current_color = color['yellow']
        else:
            current_color = color['black']

        pygame.draw.rect(display_surface, current_color, (x,y,sprite_width,sprite_height))

        pygame . display . flip()
        clock . tick (90)
    pygame . quit ()

if __name__ == '__main__':
    main()