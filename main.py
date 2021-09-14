####################################
#             IMPORTS              #
####################################

import pygame # The library used for all of the graphics
import pickle # For easy saving and loading of object data
from datetime import date # For exporting data with the date as the file name

####################################
#          PROJECT SETUP           #
####################################

pygame.init()
pygame.font.init()

####################################
#         GLOBAL VARIABLES         #
####################################

width = 550
height = 230
title = "Helpdesk Ticket Tracker"

percentFill = (150, 140, 235)
averageFill = (251, 244, 106)
helpdeskFill = (243, 85, 119)

####################################
#          BUTTON CLASS            #
####################################

class Button():
    def __init__(self, x, y, width, height, image, function):
        self.x = x
        self.y = y

        self.width = width
        self.height = height

        self.image = image

        self.function = function

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

    def update(self, events):
        pos = pygame.mouse.get_pos()

        if self.x <= pos[0] <= self.x + self.width:
            if self.y <= pos[1] <= self.y + self.height:
                for event in events:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.function()

####################################
#          SLIDER CLASS            #
####################################

class Slider():
    def __init__(self):
        self.x = 25
        self.y = 30

        self.width = 500
        self.height = 35

        self.value = 0
        self.fill = int(self.value * 5)

    def draw(self, surface):
        pygame.draw.rect(surface, percentFill, (self.x, self.y, self.fill, self.height))

    def update(self):
        self.fill = int(self.value * 5)

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

        self.font = pygame.font.Font("assets/fonts/VT323/VT323-Regular.ttf", 40)

        self.value = 60
        self.offset = int(self.value * 5)

        self.valueText = self.font.render(str(self.value), False, averageFill)

        self.incButton = Button(400, 110, 50, 15, pygame.image.load("assets/ui/buttons/averageIncButton.png"), self.incValue)
        self.decButton = Button(400, 190, 50, 15, pygame.image.load("assets/ui/buttons/averageDecButton.png"), self.decValue)

        self.saveButton = Button(475, 110, 50, 35, pygame.image.load("assets/ui/buttons/averageSaveButton.png"), self.saveValue)
        self.loadButton = Button(475, 170, 50, 35, pygame.image.load("assets/ui/buttons/averageLoadButton.png"), self.loadValue)

    def draw(self, surface):
        surface.blit(self.image, (self.x + self.offset, self.y))
        surface.blit(self.valueText, (409, 137))

        self.incButton.draw(surface)
        self.decButton.draw(surface)
        self.saveButton.draw(surface)
        self.loadButton.draw(surface)

    def update(self, events):
        self.offset = int(self.value * 5)
        self.valueText = self.font.render(str(self.value), True, averageFill)

        self.incButton.update(events)
        self.decButton.update(events)
        self.saveButton.update(events)
        self.loadButton.update(events)

    def incValue(self):
        if self.value < 100:
            self.value += 1

    def decValue(self):
        if self.value > 1:
            self.value -= 1

    def saveValue(self):
        pickle.dump(self.value, open("data/average/value.p", "wb"))

    def loadValue(self):
        self.value = pickle.load(open("data/average/value.p", "rb"))

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

        self.font = pygame.font.Font("assets/fonts/VT323/VT323-Regular.ttf", 32)

        self.filename = ""

        self.slider = Slider()
        self.average = Average()

        self.inpersonTickets = 0
        self.helpdeskTickets = 0

        self.percentNonHelpdesk = 0

        self.inpersonTicketText = self.font.render(str(self.inpersonTickets), True, percentFill)
        self.helpdeskTicketText = self.font.render(str(self.helpdeskTickets), True, helpdeskFill)

        self.totalTickets = int(self.inpersonTickets + self.helpdeskTickets)

        try:
            self.percentNonHelpdesk = int(self.inpersonTickets / self.totalTickets) * 100
        except:
            pass

        self.inpersonButton = Button(25, 110, 100, 35, pygame.image.load("assets/ui/buttons/inpersonButton.png"), self.incInpersonTickets)
        self.helpdeskButton = Button(150, 110, 100, 35, pygame.image.load("assets/ui/buttons/helpdeskButton.png"), self.incHelpdeskTickets)

        self.saveButton = Button(25, 170, 100, 35, pygame.image.load("assets/ui/buttons/saveButton.png"), self.saveData)
        self.loadButton = Button(150, 170, 100, 35, pygame.image.load("assets/ui/buttons/loadButton.png"), self.loadData)
        self.exportButton = Button(275, 170, 100, 35, pygame.image.load("assets/ui/buttons/exportButton.png"), self.exportData)

    def incInpersonTickets(self):
        self.inpersonTickets += 1

    def incHelpdeskTickets(self):
        self.helpdeskTickets += 1

    def saveData(self):
        pickle.dump(self.helpdeskTickets, open("data/tickets/helpdeskTickets.p", "wb"))
        pickle.dump(self.inpersonTickets, open("data/tickets/inpersonTickets.p", "wb"))

    def loadData(self):
        self.helpdeskTickets = pickle.load(open("data/tickets/helpdeskTickets.p", "rb"))
        self.inpersonTickets = pickle.load(open("data/tickets/inpersonTickets.p", "rb"))

    def exportData(self):
        getDay = date.today()
        today = getDay.strftime("%m-%d-%y")
        self.filename = str("data/exports/" + today + ".txt")

        with open(self.filename, "w") as file:
            file.write("\n")
            file.write("Helpdesk Tickets: " + str(self.helpdeskTickets) + "\n")
            file.write("In-person Tickets: " + str(self.inpersonTickets) + "\n")
            file.write("Total Tickets: " + str(self.totalTickets) + "\n")
            file.write("\n")
            file.write("Percent of non Helpdesk Tickets: " + str(self.percentNonHelpdesk) + "%" + "\n")

    def start(self):
        self.average.loadValue()
        self.loadData()

        while self.running:
            self.events = pygame.event.get()

            for event in self.events:
                if event.type == pygame.QUIT:
                    self.average.saveData()
                    self.saveData()
                    self.running = False

            self.draw()

            self.update()

    def draw(self):
        self.screen.blit(self.background, (0, 0))

        self.slider.draw(self.screen)
        self.average.draw(self.screen)

        self.inpersonButton.draw(self.screen)
        self.helpdeskButton.draw(self.screen)

        self.saveButton.draw(self.screen)
        self.loadButton.draw(self.screen)
        self.exportButton.draw(self.screen)

        if self.inpersonTickets < 10:
            self.screen.blit(self.inpersonTicketText, (288, 110))
        else:
            self.screen.blit(self.inpersonTicketText, (282, 110))

        if self.helpdeskTickets < 10:
            self.screen.blit(self.helpdeskTicketText, (348, 110))
        else:
            self.screen.blit(self.helpdeskTicketText, (342, 110))

    def update(self):
        self.average.update(self.events)

        self.totalTickets = int(self.inpersonTickets + self.helpdeskTickets)

        try:
            self.percentNonHelpdesk = int((self.inpersonTickets / self.totalTickets) * 100)
        except:
            pass

        self.slider.value = self.percentNonHelpdesk
        self.slider.update()

        self.inpersonButton.update(self.events)
        self.helpdeskButton.update(self.events)

        self.saveButton.update(self.events)
        self.loadButton.update(self.events)
        self.exportButton.update(self.events)

        self.inpersonTicketText = self.font.render(str(self.inpersonTickets), True, percentFill)
        self.helpdeskTicketText = self.font.render(str(self.helpdeskTickets), True, helpdeskFill)

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
