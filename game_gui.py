import pygame
from computer import Computer
from human import Human


class Game(object):

    def __init__(self):
        self.next_button = pygame.Rect(458, 595, 92, 34)
        self.human = Human()
        self.computer = Computer()
        pygame.init()  # always do this at the beginning of ur program)
        self.win = pygame.display.set_mode((1024, 768))  # sets ur window
        self.background = pygame.image.load("background main.png")
        pygame.display.set_caption("Battleship Game")  # names the window

    def play(self):
        self.win.blit(self.background, (0, 0))
        # make boards
        self.computer.make_board(self.win, 47, 200)
        self.human.make_board(self.win, 594, 200)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False  # stops the program when u hit the x
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.next_button.collidepoint(event.pos):




Game().play()
