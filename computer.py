import random

from player import Player


class Computer(Player):

    def __init__(self):
        super().__init__()
        # etc.

        fired_here = []
        self.fired_here = fired_here

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

    def random_attack(self, human):
        random_attack = self.get_coords()
        while random_attack in self.fired_here:
            random_attack = self.get_coords()
        print("The computer has fired at " + str(chr(random_attack[0] + ord("A"))) + str(random_attack[1]))
        if human.board[random_attack[0]][random_attack[1]] == "*":
            human.remove_ship(random_attack[0], random_attack[1])
            print("The computer has hit one of your ships! You still have", human.num_ships, "remaining.")

        else:
            print("The computer has missed your ship.")

        self.fired_here.append(random_attack)


