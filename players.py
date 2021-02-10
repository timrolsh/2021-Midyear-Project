import random


class Player:
# TODO, make this class contain player's board, amount of ships that they have
#  add the lost function which returns either True or False
#  add a function that builds the board for the player
#  add an add_ship function which updates empty ship slot to filled ship slot
#  add a remove_ship (full ship slot to empty) ###



    def __init__(self):
        pass

    def make_board(self):
        pass

    def add_ship(self):
        pass

    def remove_ship(self):
        pass

    def lost(self):
        pass
         
    # Computer which has the properties num_ships, board
        # 
    

###### COMPUTER FUNCTIONS #############################################

class Computer():
#TODO make it contain place_battleships(randomly places ships across the board, updates human's board, doesn't go in the
# same spot twice
# contains make a move(check to make sure it wont go to the same spot twice)


    def __init__(self, num_ships, board):
        self.num_ships = num_ships
        self.board = board

    

    def place_battleships(self):
        # generates a location for the battleship randomly that works
        runs = 0
        self.runs = runs
        

        while self.runs < 5:

            x = random.randrange(0, 10)
            y = random.randrange(0, 8)

            if self.cboard[x][y] == " ":
                self.cboard[x][y] = "*"
                self.runs += 1

    def make_a_move(self, human):
        # computer will decide on a move from here
        a = random.randrange(0, 10)
        b = random.randrange(0, 8)

        if self.hboard[a][b] == "*":
            human.num_ships -= 1
            print("The computer has destroyed your ship! You have", human.num_ships, "remaining.")
            self.hboard[a][b] = " "

        elif self.hboard[a][b] == " ":
            print("Missed.")

### HUMAN FUNCTIONS #############
    
class Human():
#TODO add place_battleships(takes user's input and updates the board with add_ship)
# contains make a move(takes user's input and updated the computer's board if it hits)
# This class will eventually contain a GUi function, maybe we can put it somewhere else idk
    def __init__(self, num_ships, board):
        self.num_ships = num_ships
        self.board = board
        

        
        for x in range (self.height):
            self.hboard.append([" "] * self.width)
        

    def make_a_move(self, computer): 
            move = input('Your move: ').upper()

            if len(move) != 2:
                print("Invalid input, try something like (A1).")
            
            letter = move[0]
            
            if letter not in "ABCDEFGH":
                print("Invalid letter input, try A-H")
            
            y = ord(letter) - ord("A")
            number = move[1]
            
            if number not in "0123456789":
                print("Invalid number, try from 0-9")
            
            x = int(number)

            if self.cboard[x][y] == "*":
                computer.runs -= 1
                print("You have destroyed the computer's ship!", computer.runs, " more ships to go!")
                self.cboard[x][y] == " "
            elif self.cboard[x][y] == " ":
                print("Missed.")




    def place_battleships(self):
        self.num_ships = 0
        
        
        while self.num_ships < 5:
            
            ship_placement = input("Coordinates to your ship, Done when finished. ").upper()
            
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
            
            self.add_ship([(x, y)])
            self.num_ships +=1
            

        for x in self.hboard:
            print(x, "\n")



            


