# this allows us to use code from
# the open-source pygame library
# throughout this file

import pygame

import sys

from asteroidfield import *

from player import *

from asteroid import *

from constants import * #(SCREEN_WIDTH, importing with wild car for now
                       #SCREEN_HEIGHT, 
                       #ASTEROID_MIN_RADIUS, 
                       #ASTEROID_KINDS,
                       #ASTEROID_SPAWN_RATE,
                       #ASTEROID_MAX_RADIUS)

#updatable = pygame.sprite.Group()
#drawable = pygame.sprite.Group()
#Player.containers = (updatable, drawable)

def main():
    pygame.init()
    font = pygame.font.Font(None, 36)
    score = 0
    asteroid_group = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroid_group, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots,)
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    asteroids_field = AsteroidField() 
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}") 
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen.fill(color="black")
    text_surface = font.render(f"Welcome to Asteroids", True, "white")
    screen.blit(text_surface, (((SCREEN_WIDTH * 0.5) - (text_surface.get_width() / 2), (SCREEN_HEIGHT*0.5) - 20)))
    pygame.display.flip()
    pygame.time.wait(1000)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(60)/1000       
        screen.fill(color="black")
        updatable.update(dt)
        shots.update(dt)
        for asteroid in asteroid_group:
            if player.collison(asteroid) == True:
                print("Game over!")
                text_surface = font.render("Gamer over!", True, "white")
                screen.blit(text_surface, (((SCREEN_WIDTH * 0.5) - (text_surface.get_width() / 2), (SCREEN_HEIGHT*0.5) - 20)))
                text_surface = font.render(f"you got {score}", True, "white")
                screen.blit(text_surface, (((SCREEN_WIDTH * 0.5) - (text_surface.get_width() / 2), SCREEN_HEIGHT*0.5 + 20)))
                pygame.display.flip()
                pygame.time.wait(3000)  
                sys.exit()
        for asteroid in asteroid_group:
            for shot in shots:
                if shot.collison(asteroid):
                    shot.kill()
                    if asteroid.radius == 60:
                        score += 1 
                    elif asteroid.radius == 40:
                        score += 3
                    else:
                        score +=7
                    asteroid.split()            
        for sprite in drawable:
            sprite.draw(screen)  
        for bullet in shots:
            bullet.draw(screen)
        text_surface = font.render(f"Current score: {score}!", True, "white")
        screen.blit(text_surface, ((SCREEN_WIDTH - text_surface.get_width()), 10))
        pygame.display.flip()


if __name__ == "__main__":
    main()
