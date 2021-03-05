from computer import Computer
from human import Human


class Game(object):
    """
    ################### Characters ###################
    """

    def __init__(self):

        self.human = Human()
        self.computer = Computer()

    def play(self):

        # Make Boards

        self.computer.make_board()
        self.human.make_board()

        # Place the Ships
        print("Welcome to the Battleship game! You will play the comuter until one of you destroys the opponent's "
              "ship. First one to do so wins! Each player will have 5 ships. Let's start. \nPick your ships!")
        self.computer.place_battleships()
        self.human.place_battleships()
        print("Your board: \n    A    B    C    D    E    F    G    H")
        self.human.print_board()

        print("Congrats! You have placed your ships. Your board is displayed above. Your computer has also picked out "
              "five random locations for its ships. ")
        while not self.human.lost() and not self.computer.lost():
            self.human.user_attack(self.computer)

            if self.computer.lost():
                break
            print("Computer's move. ")
            self.computer.random_attack(self.human)

            print("Your board: \n    A    B    C    D    E    F    G    H")
            self.human.print_board()

        if self.computer.lost():
            print("Congrats! You have won!")
        else:
            print("The computer has destroyed all of your ships, you lose. ")


Game().play()
