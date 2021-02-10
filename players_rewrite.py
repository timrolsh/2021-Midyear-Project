import random


class Player(object):

    def __init__(self, board, num_ships, width, height):
        # board is an empty list for now
        board = []
        self.board = board

        # number of ships that the board currently has, goes up to 5 and will decrease when ships get destroyed
        num_ships = 0
        self.num_ships = num_ships

        width = 8  # values A(0) B(1) ..... H(7) !!! Y VALUE !!!
        height = 10  # values 0,9 !!! X VALUE !!! THESE ARE FLIPPED
        self.width = width
        self.height = height

    def make_board(self):  # takes the empty list we made earlier and turns it into a board
        for x in range(self.height):
            self.board.append([" "] * self.width)  # change this if board doesn't work

    def add_ship(self, x, y):  # updates an empty ship slot on the board to a full ship slot
        self.board[x][y] = "ship"
        self.num_ships += 1

    def remove_ship(self, x, y):  # updates a full ship slot on the board to an empty ship slot
        self.board[x][y] = " "
        self.num_ships -= 1

    def lost(self):  # returns True if the player's ship count is at 0, meaning all of their ships are destroyed
        if self.num_ships == 0:
            return True


class Human(Player):
    def __init__(self):
        super().__init__()  # TODO in pycharm this is giving me a lot of errors saying "Parameter 'board' unfilled",
        # etc.

    # user input function
    # place battleships function
    # make a move /attack function

    def user_input(self):
        while self.num_ships < 5:

            ship_placement = input("Input coordinates to ship").upper()

            if ship_placement == "DONE":
                break

            if len(ship_placement) != 2:
                print("Invalid input, try something like (A1).")

            letter = ship_placement[0]

            if letter not in "ABCDEFGH":
                print("Invalid letter input, try A-H")

            y = ord(letter) - ord("A")
            number = ship_placement[1]

            if number not in "0123456789":
                print("Invalid number, try from 0-9")

            x = int(number)

            return x, y

    def place_battleships(self):

        while self.num_ships < 5:
            placement = self.user_input()
            self.add_ship(placement)

    def user_attack(self, computer):
        attack = self.user_input()
        if computer.board[attack] == "ship":
            computer.remove_ship(attack)
            print("You have sunk the computer's ship!", computer.num_ships, "more ships left to destroy. ")

        # checks if the user's input is a spot on the computer's board, if that's true then it removes the ship,
        # also prints congrats message with computer.num_ships


class Computer(Player):  # TODO finish writing the methods for this class
    def __init__(self):
        super().__init__()  # TODO in pycharm this is giving me a lot of errors saying "Parameter 'board' unfilled",
        # etc.

    # place battleships function
    # make a move function/attack function

    def place_battleships(self, x, y):
        pass
        # takes randomly generated set of coordinates from get_coordinates function, checks to see if there is already a
        # ship there and if there isn't it will add a ship

    def get_coordinates(self):
        pass
        # should use random.randrange to get coordinates for attack

    def random_attack(self):
        pass
        # should use get_coordinates to get coordinates for attack, then make the attack using the board from human
