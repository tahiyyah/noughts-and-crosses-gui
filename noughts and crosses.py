# noughts and crosses
import pygame
from pygame import *

pygame.init() #initialising pygame

screen_width = 600 #dimensions
screen_height = 700

player = 'x'
play = True

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("noughts & crosses") #game name
clock = pygame.time.Clock()

board_colour = (255, 246, 178)
board_colour2 = (212, 206, 150)
board_edge_colour = (134, 104, 4)

board = [[None, None, None],
         [None, None, None],
         [None, None, None],
        ]

class Button: #creates button class
    def __init__(self, x_pos, y_pos, width, height, base_colour, hover_colour, enabled):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.height = height
        self.base_colour = base_colour
        self.hover_colour = hover_colour
        self.enabled = enabled
        self.draw() #draws button to screen automatically

    def draw(self): #draws button to screen
        button_rect = pygame.rect.Rect((self.x_pos, self.y_pos), (self.width, self.height)) #creates rectangle that is the button

        if self.enabled: #if enabled = True
            if self.hover():   
                pygame.draw.rect(screen, self.hover_colour, button_rect, 0, 3) #changes colour when clicked
            else:
                pygame.draw.rect(screen, self.base_colour, button_rect, 0, 3)
        else:
            pygame.draw.rect(screen, self.base_colour, button_rect, 0, 3) #if enabled is false, will not change colour when clicked

    def hover(self):
        button_rect = pygame.rect.Rect((self.x_pos, self.y_pos), (self.width, self.height))
        mouse_pos = pygame.mouse.get_pos()
        if button_rect.collidepoint(mouse_pos) and self.enabled:
            return True
        else:
            return False

    def clicked(self): #checks if button gets clicked
        mouse_pos = pygame.mouse.get_pos()
        left_click = pygame.mouse.get_pressed()[0]
        button_rect = pygame.rect.Rect((self.x_pos, self.y_pos), (self.width, self.height))

        if left_click and button_rect.collidepoint(mouse_pos) and self.enabled:
            return True
        else:
            return False

def write(message, size, colour, x_pos, y_pos): #creates function for writing text to screen
    font = pygame.font.SysFont('Arial', size)
    text = font.render(message, True, colour)
    screen.blit(text, (x_pos, y_pos))

def switch():
    global player
    if player == 'x':
        player = 'o' 
    elif player == 'o':
        player = 'x'

def display():
    if board[0][0] != None: #displaying player symbol on board
        write(board[0][0], 200, 'black', 60, 65)
    if board[0][1] != None:
        write(board[0][1], 200, 'black', 260, 65)
    if board[0][2] != None:
        write(board[0][2], 200, 'black', 460, 65)
    if board[1][0] != None:
        write(board[1][0], 200, 'black', 60, 260)
    if board[1][1] != None:
        write(board[1][1], 200, 'black', 260, 260)
    if board[1][2] != None:
        write(board[1][2], 200, 'black', 460, 260)
    if board[2][0] != None:
        write(board[2][0], 200, 'black', 60, 460)
    if board[2][1] != None:
        write(board[2][1], 200, 'black', 260, 460)
    if board[2][2] != None:
        write(board[2][2], 200, 'black', 460, 460)

def deactivate_buttons():
    global board_pos1
    global board_pos2
    global board_pos3
    global board_pos4
    global board_pos5
    global board_pos6
    global board_pos7
    global board_pos8
    global board_pos9

    board_pos1 = Button(5, 105, 195, 195, board_colour, board_colour2, False) #makes all buttons inactive
    board_pos2 = Button(205, 105, 195, 195, board_colour, board_colour2, False)
    board_pos3 = Button(405, 105, 190, 195, board_colour, board_colour2, False)
    board_pos4 = Button(5, 305, 195, 195, board_colour, board_colour2, False)
    board_pos5 = Button(205, 305, 195, 195, board_colour, board_colour2, False)
    board_pos6 = Button(405, 305, 190, 195, board_colour, board_colour2, False)
    board_pos7 = Button(5, 505, 195, 190, board_colour, board_colour2, False)
    board_pos8 = Button(205, 505, 195, 190, board_colour, board_colour2, False)
    board_pos9 = Button(405, 505, 190, 190, board_colour, board_colour2, False)

def reset():
    global board
    board = [[None, None, None],
         [None, None, None],
         [None, None, None],
        ]
    
    global player
    player = 'x'

    global play
    play = True

    main()

def check_reset():
    if restart.clicked():
        reset()

def check():
    global play
    global restart
    empty = 0
    for row in board:
        for column in row:
            if column == None:
                empty += 1 #increments empty for every empty space

    if empty == 0:
        pygame.draw.rect(screen, 'black', pygame.Rect(0, 0, 700, 100)) #game over if no empty spaces left
        write('GAME OVER', 50, 'red', 190, 25)
        deactivate_buttons()
        display()
        restart = Button(225, 375, 150, 50, 'lightpink', 'pink', True)
        write('restart?', 40, 'red', 245, 375)
        check_reset()

    if board[0][0] == 'x' and board[0][1] == 'x' and board[0][2] == 'x': #checks all winning combos
        pygame.draw.rect(screen, 'black', pygame.Rect(0, 0, 700, 100))
        write('player 1 wins!', 60, 'red', 150, 15)
        deactivate_buttons()
        play = False #ensures no more moves can be made
        display()
        restart = Button(225, 375, 150, 50, 'lightpink', 'pink', True)
        write('restart?', 40, 'red', 245, 375)
        check_reset()
    elif board[0][0] == 'o' and board[0][1] == 'o' and board[0][2] == 'o':
        pygame.draw.rect(screen, 'black', pygame.Rect(0, 0, 700, 100))
        write('player 2 wins!', 60, 'red', 150, 15)
        deactivate_buttons()
        play = False
        display()
        restart = Button(225, 375, 150, 50, 'lightpink', 'pink', True)
        write('restart?', 40, 'red', 245, 375)
        check_reset()
    elif board[1][0] == 'x' and board[1][1] == 'x' and board[1][2] == 'x':
        pygame.draw.rect(screen, 'black', pygame.Rect(0, 0, 700, 100))
        write('player 1 wins!', 60, 'red', 150, 15)
        deactivate_buttons()
        play = False
        display()
        restart = Button(225, 375, 150, 50, 'lightpink', 'pink', True)
        write('restart?', 40, 'red', 245, 375)
        check_reset()
    elif board[1][0] == 'o' and board[1][1] == 'o' and board[1][2] == 'o':
        pygame.draw.rect(screen, 'black', pygame.Rect(0, 0, 700, 100))
        write('player 2 wins!', 60, 'red', 150, 15)
        deactivate_buttons()
        play = False
        display()
        restart = Button(225, 375, 150, 50, 'lightpink', 'pink', True)
        write('restart?', 40, 'red', 245, 375)
        check_reset()
    elif board[2][0] == 'x' and board[2][1] == 'x' and board[2][2] == 'x':
        pygame.draw.rect(screen, 'black', pygame.Rect(0, 0, 700, 100))
        write('player 1 wins!', 60, 'red', 150, 15)
        deactivate_buttons()
        play = False
        display()
        restart = Button(225, 375, 150, 50, 'lightpink', 'pink', True)
        write('restart?', 40, 'red', 245, 375)
        check_reset()
    elif board[2][0] == 'o' and board[2][1] == 'o' and board[2][2] == 'o':
        pygame.draw.rect(screen, 'black', pygame.Rect(0, 0, 700, 100))
        write('player 2 wins!', 60, 'red', 150, 15)
        deactivate_buttons()
        play = False
        display()
        restart = Button(225, 375, 150, 50, 'lightpink', 'pink', True)
        write('restart?', 40, 'red', 245, 375)
        check_reset()
    elif board[0][0] == 'x' and board[1][0] == 'x' and board[2][0] == 'x':
        pygame.draw.rect(screen, 'black', pygame.Rect(0, 0, 700, 100))
        write('player 1 wins!', 60, 'red', 150, 15)
        deactivate_buttons()
        play = False
        display()
        restart = Button(225, 375, 150, 50, 'lightpink', 'pink', True)
        write('restart?', 40, 'red', 245, 375)
        check_reset()
    elif board[0][0] == '0' and board[1][0] == 'o' and board[2][0] == 'o':
        pygame.draw.rect(screen, 'black', pygame.Rect(0, 0, 700, 100))
        write('player 2 wins!', 60, 'red', 150, 15)
        deactivate_buttons()
        play = False
        display()
        restart = Button(225, 375, 150, 50, 'lightpink', 'pink', True)
        write('restart?', 40, 'red', 245, 375)
        check_reset()
    elif board[0][1] == 'x' and board[1][1] == 'x' and board[2][1] == 'x':
        pygame.draw.rect(screen, 'black', pygame.Rect(0, 0, 700, 100))
        write('player 1 wins!', 60, 'red', 150, 15)
        deactivate_buttons()
        play = False
        display()
        restart = Button(225, 375, 150, 50, 'lightpink', 'pink', True)
        write('restart?', 40, 'red', 245, 375)
        check_reset()
    elif board[0][1] == 'o' and board[1][1] == 'o' and board[2][1] == 'o':
        pygame.draw.rect(screen, 'black', pygame.Rect(0, 0, 700, 100))
        write('player 2 wins!', 60, 'red', 150, 15)
        deactivate_buttons()
        play = False
        display()
        restart = Button(225, 375, 150, 50, 'lightpink', 'pink', True)
        write('restart?', 40, 'red', 245, 375)
        check_reset()
    elif board[0][2] == 'x' and board[1][2] == 'x' and board[2][2] == 'x':
        pygame.draw.rect(screen, 'black', pygame.Rect(0, 0, 700, 100))
        write('player 1 wins!', 60, 'red', 150, 15)
        deactivate_buttons()
        play = False
        display()
        restart = Button(225, 375, 150, 50, 'lightpink', 'pink', True)
        write('restart?', 40, 'red', 245, 375)
        check_reset()
    elif board[0][2] == 'o' and board[1][2] == 'o' and board[2][2] == 'o':
        pygame.draw.rect(screen, 'black', pygame.Rect(0, 0, 700, 100))
        write('player 2 wins!', 60, 'red', 150, 15)
        deactivate_buttons()
        play = False
        display()
        restart = Button(225, 375, 150, 50, 'lightpink', 'pink', True)
        write('restart?', 40, 'red', 245, 375)
        check_reset()
    elif board[0][0] == 'x' and board[1][1] == 'x' and board[2][2] == 'x':
        pygame.draw.rect(screen, 'black', pygame.Rect(0, 0, 700, 100))
        write('player 1 wins!', 60, 'red', 150, 15)
        deactivate_buttons()
        play = False
        display()
        restart = Button(225, 375, 150, 50, 'lightpink', 'pink', True)
        write('restart?', 40, 'red', 245, 375)
        check_reset()
    elif board[0][0] == 'o' and board[1][1] == 'o' and board[2][2] == 'o':
        pygame.draw.rect(screen, 'black', pygame.Rect(0, 0, 700, 100))
        write('player 2 wins!', 60, 'red', 150, 15)
        deactivate_buttons()
        play = False
        display()
        restart = Button(225, 375, 150, 50, 'lightpink', 'pink', True)
        write('restart?', 40, 'red', 245, 375)
        check_reset()
    elif board[2][0] == 'x' and board[1][1] == 'x' and board[0][2] == 'x':
        pygame.draw.rect(screen, 'black', pygame.Rect(0, 0, 700, 100))
        write('player 1 wins!', 60, 'red', 150, 15)
        deactivate_buttons()
        play = False
        display()
        restart = Button(225, 375, 150, 50, 'lightpink', 'pink', True)
        write('restart?', 40, 'red', 245, 375)
        check_reset()
    elif board[2][0] == 'o' and board[1][1] == 'o' and board[0][2] == 'o':
        pygame.draw.rect(screen, 'black', pygame.Rect(0, 0, 700, 100))
        write('player 2 wins!', 60, 'red', 150, 15)
        deactivate_buttons()
        play = False
        display()
        restart = Button(225, 375, 150, 50, 'lightpink', 'pink', True)
        write('restart?', 40, 'red', 245, 375)

def main(): #game loop
    while True:

        #draw to screen
        screen.fill(board_colour)
        pygame.draw.rect(screen, 'pink', pygame.Rect(0, 0, 600, 100)) #creating grid    
        pygame.draw.rect(screen, board_edge_colour, pygame.Rect(200, 100, 5, 600))
        pygame.draw.rect(screen, board_edge_colour, pygame.Rect(400, 100, 5, 600))
        pygame.draw.rect(screen, board_edge_colour, pygame.Rect(0, 100, 5, 600))
        pygame.draw.rect(screen, board_edge_colour, pygame.Rect(595, 100, 5, 600))
        pygame.draw.rect(screen, board_edge_colour, pygame.Rect(0, 100, 600, 5))
        pygame.draw.rect(screen, board_edge_colour, pygame.Rect(0, 300, 600, 5))
        pygame.draw.rect(screen, board_edge_colour, pygame.Rect(0, 500, 600, 5))
        pygame.draw.rect(screen, board_edge_colour, pygame.Rect(0, 695, 600, 5))

        board_pos1 = Button(5, 105, 195, 195, board_colour, board_colour2, True) 
        board_pos2 = Button(205, 105, 195, 195, board_colour, board_colour2, True)
        board_pos3 = Button(405, 105, 190, 195, board_colour, board_colour2, True)
        board_pos4 = Button(5, 305, 195, 195, board_colour, board_colour2, True)
        board_pos5 = Button(205, 305, 195, 195, board_colour, board_colour2, True)
        board_pos6 = Button(405, 305, 190, 195, board_colour, board_colour2, True)
        board_pos7 = Button(5, 505, 195, 190, board_colour, board_colour2, True)
        board_pos8 = Button(205, 505, 195, 190, board_colour, board_colour2, True)
        board_pos9 = Button(405, 505, 190, 190, board_colour, board_colour2, True)

        if player == 'x':
            write('player 1 (x) turn', 50, 'black', 150, 20) #informing player of turns
        if player == 'o':
            write('player 2 (o) turn', 50, 'black', 150, 20)

        display()

        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if board_pos1.clicked() and board[0][0] == None and play: #checks if position is empty, if it is places player symbol
                    board[0][0] = player
                    switch()
                if board_pos2.clicked() and board[0][1] == None and play:
                    board[0][1] = player
                    switch()
                if board_pos3.clicked() and board[0][2] == None and play:
                    board[0][2] = player
                    switch()
                if board_pos4.clicked() and board[1][0] == None and play:
                    board[1][0] = player
                    switch()
                if board_pos5.clicked() and board[1][1] == None and play:
                    board[1][1] = player
                    switch()
                if board_pos6.clicked() and board[1][2] == None and play:
                    board[1][2] = player
                    switch()
                if board_pos7.clicked() and board[2][0] == None and play:
                    board[2][0] = player
                    switch()
                if board_pos8.clicked() and board[2][1] == None and play:
                    board[2][1] = player
                    switch()
                if board_pos9.clicked() and board[2][2] == None and play:
                    board[2][2] = player
                    switch()
            if event.type == pygame.QUIT: #checks if the 'x' button is pressed
                pygame.quit()

        check()

        pygame.display.update()
main()

pygame.quit()
