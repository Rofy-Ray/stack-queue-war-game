########################################################################################################################
# Author: Raymond Okyere-Forson
# Username: okyereforsonr
#
# Assignment: Extra Credit Project - Enhanced Stacks & Queues Card War Game
#
# Purpose: Working with easygui to use stacks and queues in playing the card game.
########################################################################################################################
# Acknowledgements: Aaron Christson & Jamal Aw Yoonis
#
########################################################################################################################

import time


class Display:

    def __init__(self):
        self.user = None
        self.computer = None

    def draw_board(self, wn,  turt):            # This method serves to position the board game and draw it
        """Draws the game board"""
        turt.hideturtle()
        turt.color('gray')
        turt.penup()
        turt.setpos(-200, 200)
        turt.pendown()
        turt.begin_fill()
        for i in range(4):
            turt.fd(400)
            turt.right(90)
        turt.end_fill()

    def user_playing(self, wn, turt):           # This card draws the number of cards in the playing pile and it display on the baord game
        """Draws the user playing pile"""
        turt.hideturtle()
        turt.color('blue')
        turt.penup()
        turt.setpos(100, -100)              # this sets up the position of the card image in the game baord
        turt.pendown()
        turt.begin_fill()
        for i in range(2):
            turt.fd(50)
            turt.right(90)
            turt.fd(70)
            turt.right(90)
        turt.end_fill()

    def comp_storage(self, wn, turt):               # This method draws the number of cards in the user's pile and it display how many of them are in the pile each round
        """Draws the user storage pile"""
        turt.penup()
        turt.setpos(100, 165)
        turt.pendown()
        turt.begin_fill()
        for i in range(2):          # this is where the image is drawn
            turt.fd(50)
            turt.right(90)
            turt.fd(70)
            turt.right(90)
        turt.end_fill()

    def user_storage(self, wn, turt):       # this method draws the numbers in the computer's pile and it displays it on the game board
        """Draws the computer playing pile"""
        turt.color('blue')
        turt.penup()
        turt.setpos(-140, -100)     # The position of the image of the pile in the game baord
        turt.pendown()
        turt.begin_fill()
        for i in range(2):
            turt.fd(50)
            turt.right(90)
            turt.fd(70)
            turt.right(90)
        turt.end_fill()

    def comp_playing(self,wn , turt):       # This method serves to draw the number of cards in the computer's pile in each round of the game
        """Draws the computer storage pile"""
        turt.penup()
        turt.color('red')
        turt.setpos(-140, 165)
        turt.pendown()
        turt.begin_fill()
        for i in range(2):          # This is where the image is drawn on the board game
            turt.fd(50)
            turt.right(90)
            turt.fd(70)
            turt.right(90)
        turt.end_fill()

    def write_text(self, wn, turt):
        """Shows text on the board"""
        turt.penup()
        turt.setpos(3, -275)
        turt.pendown()
        turt.color('black')
        turt.write("Me", move = False, align = "center", font = ('Trebuchet MS', 30, 'normal'))   # writes user at the user side
        turt.penup()
        turt.setpos(3, 220)
        turt.pendown()
        turt.write("Computer", move = False, align= "center", font = ('Trebuchet MS', 30, 'normal'))  # writes computer at the computer side

    def user_card_number(self, wn, turt, num):
        """This method serves to write numbers of card in the user's deck in each round"""
        turt.hideturtle()
        turt.penup()
        turt.setpos(120, -195)
        turt.pendown()
        turt.color('blue')
        turt.write(num, move = False, align = "center", font = ('Trebuchet MS', 15, 'normal'))  # This is where you write the numbers on the image
        turt.color('white')

    def other_card_number(self, wn, turt, num):
        """This method serves to write the numbers of cards in the computer's pile in each round and then it
        displays it on the board game"""
        turt.hideturtle()
        turt.penup()
        turt.setpos(-120, 165)
        turt.pendown()
        turt.color('red')
        turt.write(num, move = False, align = "center", font = ('Trebuchet MS', 15, 'normal'))  # this is where you write the numbers of the cards in the computer's pile
        turt.color('white')

    def user_storage_number(self, wn, turt, num):
        """This method writes the numbers of cards in the user's storage and display it on the board"""
        turt.hideturtle()
        turt.penup()
        turt.setpos(-115, -100)
        turt.pendown()
        turt.color('blue')
        turt.write(num, move = False, align = "center", font = ('Trebuchet MS', 15, 'normal'))  # This is where you write number that tells you how many cards in the user's storage
        turt.color('white')

    def other_storage_number(self, wn, turt, num):
        """This method serves to write the numbers in the coputer's storage in the pile and display on the screen"""
        turt.hideturtle()
        turt.penup()
        turt.setpos(124, 163)  # The position of the numbers in the board game
        turt.pendown()
        turt.color('red')
        turt.write(num, move = False, align = "center", font = ('Trebuchet MS', 15, 'normal'))  # It enables you to write the numbers of the computer's storage in the board game
        turt.color('white')

    def play_card(self, wn, turt):
        """Animation for playing the card"""
        x = 100
        y = -100
        turt.hideturtle()
        turt.color('black')
        turt.penup()
        turt.setpos(x, y)                                   # starts the animation at the position of the playing pile
        turt.pendown()
        for x in range(4):                                  # draws the card 4 times to imply movement
            turt.clear()
            turt.penup()
            turt.setpos(x, y)
            turt.pendown()
            turt.begin_fill()
            for i in range(2):                              # draws the card
                turt.fd(50)
                turt.right(90)
                turt.fd(70)
                turt.right(90)
                x += 25                                     # updates the x value
                y += 19                                     # updates the y value
            turt.end_fill()

    def play_other_card(self, wn, turt):
        """Show the animation for playing the computer card"""
        x = -140
        y = 165
        turt.penup()
        turt.setpos(x, y)                                   # starts the animation at the computer's playing pile
        turt.pendown()
        for x in range(4):                                  # draws the card 4 times for movement
            turt.clear()
            turt.penup()
            turt.setpos(-50, y)
            turt.pendown()
            turt.begin_fill()
            for i in range(2):                              # draws card
                turt.fd(50)
                turt.right(90)
                turt.fd(70)
                turt.right(90)
                y -= 25                                     # updated the y value to move down
            turt.end_fill()

    def replace_card(self, wn, turt):
        """Shows animation to move the storage pile to the playing pile"""
        x = -140
        y = -100
        turt.penup()
        turt.setpos(x, y)                                    # starting position is the same as the user's storage pile
        turt.pendown()
        for p in range(4):                                      # draws the card 4 times
            turt.clear()
            turt.penup()
            turt.setpos(x, y)
            turt.pendown()
            turt.begin_fill()
            for i in range(2):                              # draws the card
                turt.fd(50)
                turt.right(90)
                turt.fd(70)
                turt.right(90)
                x += 28                                     # updates the x value
            turt.end_fill()

    def replace_other_card(self, wn, turt):
        """Shows the animation to move the storage pile to the computer playing pile"""
        x = 100
        y = 165
        turt.penup()
        turt.setpos(x, y)                               # start position for the animation
        turt.pendown()
        for p in range(4):                              # draws the card 4 times
            turt.clear()
            turt.penup()
            turt.setpos(x, y)
            turt.pendown()
            turt.begin_fill()
            for i in range(2):                          # draws card
                turt.fd(50)
                turt.right(90)
                turt.fd(70)
                turt.right(90)
                x -= 28                                 # decreases the x value
            turt.end_fill()

    def played_number(self, wn, turt, num):
        """Shows the number of the card played"""
        turt.hideturtle()
        turt.penup()
        turt.setpos(30, -45)                            # position of the drawing
        turt.pendown()
        turt.color('white')
        turt.write(num, move = False, align = "center", font = ('Trebuchet MS', 30, 'normal'))      # writes the number
        turt.color('white')

    def other_played_number(self, wn, turt, num):
        """Shows the number of the computer's card"""
        turt.hideturtle()
        turt.penup()
        turt.setpos(-22, -45)                           # position of the drawing
        turt.pendown()
        turt.color('black')
        turt.write(num, move = False, align = "center", font = ('Trebuchet MS', 30, 'normal'))           # writes the number
        turt.color('white')

    def win_message(self, wn, turt, win):
        """Displays the winner of the game"""
        turt.hideturtle()
        turt.penup()
        turt.setpos(-400, 20)                           # position for message
        turt.pendown()
        turt.color('black')
        turt.write(win, move = False, align = "center", font = ('Trebuchet MS', 30, 'normal'))            # writes message
        turt.color('white')
        time.sleep(5)
