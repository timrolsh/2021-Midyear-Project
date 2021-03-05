class Player(object):

    def __init__(self):

        board = []
        self.board = board

        num_ships = 0
        self.num_ships = num_ships

        width = 8  # values A(0) B(1) ..... H(7) !!! Y VALUE !!!
        height = 10  # values 0,9 !!! X VALUE !!! THESE ARE FLIPPED
        self.width = width
        self.height = height

    def make_board(self):  # takes the empty list we made earlier and turns it into a board
        for x in range(self.height):
            self.board.append([" "] * self.width)

    def add_ship(self, x, y):  # updates an empty ship slot on the board to a full ship slot
        self.board[x][y] = "*"
        self.num_ships += 1

    def remove_ship(self, x, y):  # updates a full ship slot on the board to an empty ship slot
        self.board[x][y] = " "
        self.num_ships -= 1

    def lost(self):  # returns True if the player's ship count is at 0, meaning all of their ships are destroyed
        if self.num_ships == 0:
            return True

    def print_board(self):
        for x in range(len(self.board)):
            print(x, self.board[x], "\n")
