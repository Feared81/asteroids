import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import sys


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, drawable, updatable)

    space_ship = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT /2)
    asteroid_field = AsteroidField()



    # Game loop starts
    while True:
        log_state()

        # Event queue
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
                print(f"Screen width: {SCREEN_WIDTH}")
                print(f"Screen height: {SCREEN_HEIGHT}")
                print(f"Time: {dt}")
                return

        screen.fill("black")

        updatable.update(dt)

        for thing in asteroids:
            for bullet in shots:
                if thing.collides_with(bullet):
                    log_event("asteroid_shot")
                    thing.split()
                    bullet.kill()

        for thing in asteroids:
            if thing.collides_with(space_ship):
                log_event("player_hit")
                print("Game over!")
                sys.exit()


        for thing in drawable:
            thing.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000






if __name__ == "__main__":
    main()
