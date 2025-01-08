# create a pygame window and responding to user input:
import sys
import pygame
class AlienInvasion:
    '''Overall class to manage game assets and behaviour.'''
    def __init__(self):
        pygame.init()
        self.clock=pygame.time.Clock()
        self.screen=pygame.display.setmode(1200,800)
        pygame.display.set_caption("Alien Invasion")
    def run_game(self):
        '''Start the main loop for the game.'''
        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    sys.exit()
            # make the most recently drawn screen visible.
            pygame.display.flip()
            self.clock.tick(60)






