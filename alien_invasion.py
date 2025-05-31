# create a pygame window and responding to user input:
import sys
import pygame
class AlienInvasion:
    '''Overall class to manage game assets and behaviour.'''
    def __init__(self):
        pygame.init()
        self.clock=pygame.time.Clock()
        self.screen=pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Alien Invasion")
        # setr color
        self.bg_color=(230,230,230)
    def run_game(self):
        '''Start the main loop for the game.'''
        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    sys.exit()
            # make the most recently drawn screen visible.
            self.screen.fill(self.bg_color)
            pygame.display.flip()
            self.clock.tick(60)
if __name__=='__main__':
     # make a game instance,and run the game.
    ai=AlienInvasion()
    ai.run_game()






