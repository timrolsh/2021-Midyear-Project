# from computer import Computer
# from human import Human
#
# # this doesn't work at all just leaving it in here so we can use it as a reference for next time
#
# class Game(object):
#     def __init__(self):
#         self.human = Player.human
#         self.computer = Computer()
#
#     def play(self):
#
#         self.computer.place_battleships()
#         self.human.place_battleships()
#
#         while not self.human.lost():
#             # human's move
#             self.human.make_a_move(self.computer)
#             # computer's move
#             self.computer.make_a_move(self.human)
#
#         if self.computer.lost():
#             print("You have won!")
#         elif self.human.lost():
#             print("You have lost, computer has won. ")
#
#
# Game().play()
