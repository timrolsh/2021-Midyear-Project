import random

import pygame

from player import Player


class Computer(Player):

    def __init__(self):
        super().__init__()
        # etc.

    def place_battleships(self):

        while self.num_ships < 5:

            placement = self.get_coords()

            while self.board[placement[0]][placement[1]] == '*':
                placement = self.get_coords()

            self.add_ship(placement[0], placement[1])

    def get_coords(self):
        x = random.randrange(0, self.height)
        y = random.randrange(0, self.width)

        return [x, y]

    def draw_board(self, window):
        y = 200
        for a in self.board:
            for b in range(len(a)):
                if a[b] == "f":  # TODO this might not work check it
                    window.blit(pygame.image.load("went_here.png"), (597 + b * 50, y))
                elif a[b] == "b":
                    window.blit(pygame.image.load("broken_ship.png"), (597 + b * 50, y))
                else:
                    window.blit(pygame.image.load("unknown.png"), (597 + b * 50, y))
            y += 40
