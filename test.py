import pygame

pygame.init()  # always do this at the beginning of ur program)
win = pygame.display.set_mode((1024, 768))  # sets ur window
background = pygame.image.load("background main.png")
pygame.display.set_caption("Battleship Game")  # names the window


# btw all coords start from top left
# main loop

def make_board(x, y):
    width = 35
    height = 20
    for a in range(10):
        for b in range(8):
            pygame.draw.rect(win, (104, 110, 108), (x + b * 50, y, width, height))

        y += 40





while True:
    win.blit(background, (0, 0))
    # pygame.time.delay(100)  # 100ms delay, 1000ms would be a full second, slows game down
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False  # stops the program when u hit the x
            pygame.quit()
    # pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))  # this takes input and makes a rectangle
    make_board(47, 200)
    make_board(594, 200)
    pygame.display.update()
    # pygame.display.update()  # actually shows the rectangle on the screen, updates ur display
