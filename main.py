# this allows us to use code from
# the open-source pygame library
# throughout this file

import pygame

from constants import * #(SCREEN_WIDTH, importing with wild car for now
                       #SCREEN_HEIGHT, 
                       #ASTEROID_MIN_RADIUS, 
                       #ASTEROID_KINDS,
                       #ASTEROID_SPAWN_RATE,
                       #ASTEROID_MAX_RADIUS)

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while SCREEN_WIDTH == 1280:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(color="black")
        pygame.display.flip()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}") 
    print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
