# this allows us to use code from
# the open-source pygame library
# throughout this file

import pygame

from player import *

from constants import * #(SCREEN_WIDTH, importing with wild car for now
                       #SCREEN_HEIGHT, 
                       #ASTEROID_MIN_RADIUS, 
                       #ASTEROID_KINDS,
                       #ASTEROID_SPAWN_RATE,
                       #ASTEROID_MAX_RADIUS)

def main():
    pygame.init()
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while SCREEN_WIDTH == 1280:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(60)/1000        
        screen.fill(color="black")
        player.draw(screen)
        pygame.display.flip()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}") 
    print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
