import time

import pygame
from computer import Computer
from human import Human


class Game(object):

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1024, 768))
        pygame.display.set_caption("Battleship Game")
        self.computer = Computer()
        self.human = Human()

    def play(self):
        self.computer.make_board()
        self.human.make_board()
        self.screen.blit(pygame.image.load("bg.png"), (0, 0))
        self.computer.draw_board(self.screen)
        self.human.draw_board(self.screen)
        self.message_display("Welcome to the Battleship game! You will play the comuter until one", 512, 634)
        self.message_display("of you destroys the opponent's ship. First one to do so wins! Each ", 512, 664)
        self.message_display("player will have 5 ships. Let's start. Click NEXT to Pick your ships!", 512, 694)
        pygame.display.update()
        self.next_button()
        self.place_battleships()
        self.computer.place_battleships()

        self.screen.blit(pygame.image.load("bg.png"), (0, 0))
        self.computer.draw_board(self.screen)
        self.human.draw_board(self.screen)
        self.message_display("The computer has now picked 5 random ship locations. ", 512, 634)
        self.message_display("Click NEXT to start attack. ", 512, 664)
        pygame.display.update()
        self.next_button()

        while not self.human.lost() and not self.computer.lost():
            self.user_attack(self.computer)
            self.computer_attack(self.human)

        if self.human.lost():
            self.message_display("You have lost. The computer has destroyed all of your ships. Press exit to quit. ", 512, 634)
        elif self.computer.lost():
            self.message_display("You have won! You have destroyed all of the computer's ships! Press exit to quit. ", 512, 634)
        self.exit_button()
        pygame.display.update()

    def text_objects(self, text, font):
        textSurface = font.render(text, True, (255, 255, 255))
        return textSurface, textSurface.get_rect()

    def message_display(self, text, x, y):
        output = pygame.font.Font("freesansbold.ttf", 30)
        TextSurface, TextRect = self.text_objects(text, output)
        TextRect.center = (x, y)
        self.screen.blit(TextSurface, TextRect)

    def next_button(self):
        while True:
            for event in pygame.event.get():
                pass
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            if 450 + 93 > mouse[0] > 450 and 530 + 56 > mouse[1] > 530:
                pygame.draw.rect(self.screen, (0, 255, 0), (450, 530, 93, 56))
            else:
                pygame.draw.rect(self.screen, (0, 125, 0), (450, 530, 93, 56))

            if 450 + 93 > mouse[0] > 450 and 530 + 56 > mouse[1] > 530 and click[0]:
                time.sleep(0.15)
                break
            self.message_display("Next", 450 + 93 / 2, 530 + 56 / 2)
            pygame.display.update()

    def exit_button(self):
        while True:
            for event in pygame.event.get():
                pass
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            if 450 + 93 > mouse[0] > 450 and 530 + 56 > mouse[1] > 530:
                pygame.draw.rect(self.screen, (255, 0, 0), (450, 530, 93, 56))
            else:
                pygame.draw.rect(self.screen, (125, 0, 0), (450, 530, 93, 56))

            if 450 + 93 > mouse[0] > 450 and 530 + 56 > mouse[1] > 530 and click[0]:
                time.sleep(0.1)
                break

            self.message_display("Exit", 450 + 93 / 2, 530 + 56 / 2)
            pygame.display.update()

    def place_battleships(self):
        # waits for a click
        # checks if the click is in the human's board
        # checks if the the click is in one of the squares
        # checks if the click is in a slot where there isnt a ship already
        # if it passes all of those regulations then it adds a ship

        while self.human.num_ships < 5:
            temp = False
            self.screen.blit(pygame.image.load("bg.png"), (0, 0))
            self.computer.draw_board(self.screen)
            self.human.draw_board(self.screen)
            self.message_display("%s%d%s" % (
                "Click a box on your board to place a ship. ", self.human.num_ships, " ships placed so far."), 512, 634)
            for event in pygame.event.get():
                pass
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()

            if click[0]:
                if 432 > mouse[0] > 47 and 600 > mouse[1] > 200:
                    c = 0
                    for a in self.human.board:
                        for b in range(len(a)):
                            x = 47 + b * 50
                            y = 200 + c * 40
                            if mouse[0] - x in range(35) and mouse[1] - y in range(20):
                                if a[b] == " ":
                                    a[b] = "*"
                                    self.human.num_ships += 1
                                    temp = True
                                    self.message_display(
                                        "%s%s%d" % ("Success! You have added a ship to ", chr(ord("A") + b), c), 512,
                                        664)
                                    self.human.draw_board(self.screen)
                                    self.next_button()
                        c += 1
                    if not temp:
                        self.message_display("You have clicked on an area that isnt a square. Try again", 512, 664)
                        self.next_button()
                else:
                    self.message_display("Click on an area that is on the human's board. ", 512, 664)
                    self.next_button()

            pygame.display.update()

    def user_attack(self, computer):
        # take human input and finds a spot on the computer's board
        # plays error sound if you miss, use.totem from squid pack if you land
        # prints out, you have either missed or landed the computer's ship. ___ more to go.
        # next button
        completed = False
        while not completed:
            temp = False
            self.screen.blit(pygame.image.load("bg.png"), (0, 0))
            computer.draw_board(self.screen)
            self.human.draw_board(self.screen)
            self.message_display("%s%d%s" % (
                "Click on a computer's box to attack. It has ", self.computer.num_ships, " ships remaining"), 512,
                                 634)
            for event in pygame.event.get():
                pass
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()

            if click[0]:
                if 979 > mouse[0] > 597 and 600 > mouse[1] > 200:
                    c = 0
                    for a in computer.board:
                        for b in range(len(a)):
                            x = 597 + b * 50
                            y = 200 + c * 40
                            if mouse[0] - x in range(35) and mouse[1] - y in range(20):
                                if a[b] == "*":
                                    a[b] = "b"
                                    computer.num_ships -= 1
                                    temp = True
                                    computer.draw_board(self.screen)
                                    self.message_display(
                                        "%s%s%d%s" % (
                                            "Success! You have attacked the computer at ", chr(ord("A") + b), c,
                                            " and landed!"), 512, 664)
                                    self.next_button()
                                    completed = True
                                elif a[b] == " ":
                                    a[b] = "f"
                                    temp = True
                                    self.message_display("%s%s%d%s" % (
                                        "You have attacked the computer at ", chr(ord("A") + b), c,
                                        " and you have missed."), 512, 664)
                                    self.next_button()
                                    completed = True

                        c += 1
                    if not temp:
                        self.message_display("You have clicked on an area that isnt a square. Try again", 512, 664)
                        self.next_button()
                else:
                    self.message_display("Click on an area that is on the computer's board. ", 512, 664)
                    self.next_button()

            pygame.display.update()

    def computer_attack(self, human):
        self.screen.blit(pygame.image.load("bg.png"), (0, 0))
        self.computer.draw_board(self.screen)
        human.draw_board(self.screen)
        random_attack = self.computer.get_coords()
        while human.board[random_attack[0]][random_attack[1]] == "f" or human.board[random_attack[0]][random_attack[1]] == "b":
            random_attack = self.computer.get_coords()
        if human.board[random_attack[0]][random_attack[1]] == "*":
            human.board[random_attack[0]][random_attack[1]] = "b"
            human.num_ships -= 1
            self.screen.blit(pygame.image.load("bg.png"), (0, 0))
            self.computer.draw_board(self.screen)
            human.draw_board(self.screen)
            self.message_display("%s%s%d%s" % (
                "The computer has fired at ", chr(ord("A") + random_attack[1]), random_attack[0],
                " and hit your ship!"), 512, 634)
            self.message_display("%s%d%s" % ("You still have ", human.num_ships, " remaining. "), 512, 664)
            pygame.display.update()
            self.next_button()
        else:
            human.board[random_attack[0]][random_attack[1]] = "f"
            self.screen.blit(pygame.image.load("bg.png"), (0, 0))
            self.computer.draw_board(self.screen)
            human.draw_board(self.screen)
            self.message_display("%s%s%d%s" % (
                "The computer has fired at ", chr(ord("A") + random_attack[1]), random_attack[0],
                " and missed your ship"),
                                 512, 634)
            self.message_display("%s%d%s" % ("You still have ", human.num_ships, " remaining. "), 512, 664)
            pygame.display.update()
            self.next_button()


Game().play()
