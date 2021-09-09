####################################
#             IMPORTS              #
####################################

import pygame # The library used for all of the graphics
import pickle # For easy saving and loading of object data

####################################
#          PROJECT SETUP           #
####################################

pygame.init()
pygame.font.init()

####################################
#         GLOBAL VARIABLES         #
####################################

WIDTH = 550
HEIGHT = 600
TITLE = "Helpdesk v3"

BACKGROUND = pygame.image.load("assets/ui/background/background.png")

####################################
#            MAIN CLASS            #
####################################

class Window():
    def __init__(self):
        self.screen = pygame.display.set_mode([WIDTH, HEIGHT])
        pygame.display.set_caption(TITLE)

        self.running = True
        self.clock = pygame.time.Clock()
        self.events = pygame.event.get()

    def start(self):
        while self.running:
            self.events = pygame.event.get()

            for event in self.events:
                if event.type == pygame.QUIT:
                    self.running = False

            self.draw()

            self.update()

    def draw(self):
        self.screen.blit(BACKGROUND, (0, 0))

    def update(self):
        pygame.display.update()
        self.clock.tick(30)


####################################
#          ON PROG STARTUP         #
####################################

window = Window()
window.start()

####################################
#            ON PROG QUIT          #
####################################

pygame.quit()
