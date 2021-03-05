from player import Player


class Human(Player):

    def __init__(self):
        super().__init__()

    def user_input(self, message):

        ship_placement = input(message + "\t").upper()

        while len(ship_placement) != 2 or ship_placement[0] not in "ABCDEFGH" or ship_placement[1] not in "0123456789":
            # Add check for dup placements

            print("Invalid input. Proper input is 2 characters, first one is a letter, second one should be a number: "
                  "i.e(A1)")
            ship_placement = input(message + "\t").upper()

        letter = ship_placement[0]

        y = ord(letter) - ord("A")
        number = ship_placement[1]

        x = int(number)

        return [x, y]

    def place_battleships(self):

        while self.num_ships < 5:
            placement = self.user_input("Ship coordinates(" + str(self.num_ships + 1) + "): ")

            while self.board[placement[0]][placement[1]] == '*':
                print('Already placed a ship there! Pick somewhere else to place a ship. ')
                placement = self.user_input("Ship coordinates(" + str(self.num_ships + 1) + "): ")

            self.add_ship(placement[0], placement[1])

        # for print(self.board)

    def user_attack(self, computer):

        attack = self.user_input("Your move: ")
        print("You have fired at " + str(chr(attack[0] + ord("A"))) + str(attack[1]))

        if computer.board[attack[0]][attack[1]] == "*":

            computer.remove_ship(attack[0], attack[1])
            print("You have sunk the computer's ship!", computer.num_ships, "more ships left to destroy. ")

        else:
            print("You have missed. The computer still has", computer.num_ships, "remaining. ")
