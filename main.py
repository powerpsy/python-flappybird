import pygame
import sys
from game import Game

def main():
    pygame.init()
    
    # Set up the game window
    screen_width = 1920/2
    screen_height = 1080/2
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Flappy Bird")  

    # Create a Game instance
    game = Game(screen)

    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_SPACE and not game.game_over:
                    game.bird.jump()
                if event.key == pygame.K_RETURN and game.game_over:
                    game.reset()

        game.update()
        game.draw()
        pygame.display.flip()
        pygame.time.Clock().tick(60)

if __name__ == "__main__":
    main()