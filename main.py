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

width = 550
height = 600
title = "Helpdesk v3"

percentFill = (150, 140, 235)

####################################
#          SLIDER CLASS            #
####################################

class Slider():
    def __init__(self):
        self.x = 25
        self.y = 30

        self.width = 500
        self.height = 35

        self.value = 50
        self.fill = int(self.value * 5)

    def draw(self, surface):
        pygame.draw.rect(surface, percentFill, (self.x, self.y, self.fill, self.height))

####################################
#         AVERAGE CLASS            #
####################################

class Average():
    def __init__(self):
        self.x = 23
        self.y = 14

        self.width = 500
        self.height = 35

        self.image = pygame.image.load("assets/ui/sliders/average.png")

        self.value = 60
        self.offset = int(self.value * 5)

    def draw(self, surface):
        surface.blit(self.image, (self.x + self.offset, self.y))

####################################
#            MAIN CLASS            #
####################################

class Window():
    def __init__(self):
        self.screen = pygame.display.set_mode([width, height])
        pygame.display.set_caption(title)

        self.running = True
        self.clock = pygame.time.Clock()
        self.events = pygame.event.get()

        self.background = pygame.image.load("assets/ui/background/background.png")

        self.slider = Slider()
        self.average = Average()

    def start(self):
        while self.running:
            self.events = pygame.event.get()

            for event in self.events:
                if event.type == pygame.QUIT:
                    self.running = False

            self.draw()

            self.update()

    def draw(self):
        self.screen.blit(self.background, (0, 0))

        self.slider.draw(self.screen)
        self.average.draw(self.screen)

    def update(self):
        pygame.display.update()
        self.clock.tick(30)


####################################
#          ON PROG STARTUP         #
####################################

window = Window()
window.start()

####################################
#           ON PROG QUIT           #
####################################

pygame.quit()
