import pygame
from player import Player
from circleshape import CircleShape
from logger import  log_state
from constants import SCREEN_HEIGHT,SCREEN_WIDTH
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (updatable, drawable, asteroids)
    Player.containers= (updatable, drawable)
    AsteroidField.containers = (updatable)
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()


    while(True):
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        for draw in drawable:
            draw.draw(screen)
        updatable.update(dt)
            
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        
        

if __name__ == "__main__":
    main()
