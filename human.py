from player import Player
import pygame


class Human(Player):

    def __init__(self):
        super().__init__()

    def draw_board(self, window):
        y = 200
        for a in self.board:
            for b in range(len(a)):
                if a[b] == " ":
                    window.blit(pygame.image.load("nothing.png"), (47 + b * 50, y))
                elif a[b] == "*":
                    window.blit(pygame.image.load("ship.png"), (47 + b * 50, y))
                elif a[b] == "f":  # TODO this might not work check it
                    window.blit(pygame.image.load("went_here.png"), (47 + b * 50, y))
                elif a[b] == "b":
                    window.blit(pygame.image.load("broken_ship.png"), (47 + b * 50, y))

            y += 40
