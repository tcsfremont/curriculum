""" Base window for breakout game using pygame."""
import pygame


def game():
    """Main function for the game."""

    WIDTH = 800
    HEIGHT = 600
    
    # Initialize pygame 
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Breaking Blocks")
    clock = pygame.time.Clock()

    # Game Loop
    while True:
        # Set max frames per second
        clock.tick(30)

        # Event Handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # Paint and refresh the screen
        pygame.display.flip()




if __name__ == "__main__":
    game()