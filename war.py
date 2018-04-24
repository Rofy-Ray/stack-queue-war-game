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

from myStack import Stack
from myQueue import Queue
from cards import Deck
from exhibit import Display


class War:

    def __init__(self):
        self.myCurrent = Stack()                  # my currently displayed card
        self.otherCurrent = Stack()               # other currently displayed card
        self.currentState = 0                     # keeps track of the state of play
        self.dealingPile = Stack()                # queue or stack
        self.myPlayingPile = Stack()	          # queue or stack
        self.myStoragePile = Queue()	          # queue or stack
        self.otherPlayingPile = Stack()	          # queue or stack
        self.otherStoragePile = Queue()	          # queue or stack
        self.lootPile = Stack()		              # queue or stack
        self.war = Stack()                        # holds cards in a war situation

    def add_dealingpile(self):
        """Adds the shuffled decks of cards to the dealer's pile"""
        deck = Deck()                                   # Gets deck from deck class in Cards.py
        self.dealingPile = deck.shuffle()               # Shuffles deck and stores it
        return self.dealingPile

    def deal(self, wn, turt, u_turt, x_turt):
        """Deals out 25 cards from to each player's playing pile from shuffled dealers pile """
        Display.draw_board(self, wn, turt)              # initializes board
        Display.write_text(self, wn, turt)              # initiates user and computer
        for i in range(1):                             # deals out 25 cards to player 1
            my_card = self.dealingPile.pop()
            self.myPlayingPile.push(my_card)
        Display.user_playing(self, wn, turt)            # draws user playing pile
        u_turt.clear()
        Display.user_card_number(self, wn, u_turt, self.myPlayingPile.size())       # prints number of cards

        for i in range(1):                             # deals out 25 cards to the computer
            other_card = self.dealingPile.pop()
            self.otherPlayingPile.push(other_card)
            Display.comp_playing(self, wn, turt)            # draws computer playing pile
        x_turt.clear()
        Display.other_card_number(self, wn, x_turt, self.otherPlayingPile.size())   # prints the number of cards
        return self.otherPlayingPile, self.myPlayingPile         # returns the storage for each hand

    def make_move(self, wn, turt):
        """initiates a round of play and communicates play-by-play during the round
        returns true when the game is still in play
        returns false when the game is over
        Communicates an appropriate message about whether the user beat the computer"""
        self.currentState += 1                                  # tells what round of play the game is in
        print("Round " + str(self.currentState))
        mycards = self.myPlayingPile.size()
        othercards = self.otherPlayingPile.size()
        if mycards == 0:                                        # indicates who has won
            print("Computer Won!")
            Display.win_message(self, wn, turt, 'Computer Won!')     # prints computer won
            quit()
            return False
        elif othercards == 0:
            print("You Won!")
            Display.win_message(self, wn, turt, 'You Won!')          # prints user won
            quit()
            return False
        else:
            return True

    def remove_my_card(self):
        """Precondition: myPlayingPile is not empty
        If it is not empty, the function removes a card from myPlayingPile,
        returning the stored value"""
        mycards = self.myPlayingPile.size()
        if mycards != 0:
            x = self.myPlayingPile.pop()                         # removes card from player 1 stack
            self.myCurrent.push(x)                              # puts card in the player's current card stack
            return self.myCurrent

    def remove_other_card(self):
        """Precondition: otherPlayingPile is not empty
        If it is not empty, the function removes a card from otherPlayingPile,
        returning the stored value"""
        othercards = self.otherPlayingPile.size()
        if othercards != 0:
            a = self.otherPlayingPile.pop()                     # removes card from computer stack
            self.otherCurrent.push(a)                           # puts card in the computer's current card stack
            return self.otherCurrent

    def display_card(self, wn, p_turt, c_turt):
        """Displays a card on the screen and returns the value"""
        a = self.otherCurrent.top()                             # looks at the cards in the current stack
        b = self.myCurrent.top()
        print("Computer has placed a " + str(a))
        p_turt.clear()
        Display.play_card(self, wn, p_turt)                     # displays user played card
        Display.played_number(self, wn, p_turt, b)              # displays played card number

        c_turt.clear()
        Display.play_other_card(self, wn, c_turt)               # displays computer card
        Display.other_played_number(self, wn, c_turt, a)        # displays computer card number
        print("You have placed a " + str(b))                    # prints the cards to the screen

    def compare_cards(self):
        """Compares the cards that each player plays"""
        b = self.myCurrent.top()                                # Looks at the current cards and compares them
        a = self.otherCurrent.top()
        if b > a:
            return 0
        elif b < a:
            return 1

    def compare_other(self, wn, u_turt, x_turt):
        """Gives the cards to whichever layer had the highest played number"""
        b = self.myCurrent.top()
        a = self.otherCurrent.top()

        if b > a:
            a = self.myCurrent.pop()                        # removes card and places it in the lootpile
            self.lootPile.push(a)
            x = self.otherCurrent.pop()
            self.lootPile.push(x)
            while self.war.size() != 0:                     # removes cards inside the war stack and places it in the lootpile
                p = self.war.pop()
                self.lootPile.push(p)
            u_turt.clear()
            Display.user_card_number(self, wn, u_turt, self.myPlayingPile.size())       # displays number of cards remaining for user
            x_turt.clear()
            Display.other_card_number(self, wn, x_turt, self.otherPlayingPile.size())
            print("You won the cards.")
            return self.lootPile
        elif b < a:
            b = self.myCurrent.pop()
            self.lootPile.push(b)
            c = self.otherCurrent.pop()                    # removes card and places it in the lootpile
            self.lootPile.push(c)
            while self.war.size() != 0:
                h = self.war.pop()
                self.lootPile.push(h)
            u_turt.clear()
            Display.user_card_number(self, wn, u_turt, self.myPlayingPile.size())
            x_turt.clear()
            Display.other_card_number(self, wn, x_turt, self.otherPlayingPile.size())   # displays number of cards remaining for computer
            print("Computer won the cards.")
            return self.lootPile                            # returns the lootpile
        elif b == a:
            b = self.myCurrent.pop()                        # puts the player's current card and the computer's current card in a stack if they are the same
            self.war.push(b)
            c = self.otherCurrent.pop()
            self.war.push(c)
            while self.war.size() != 0:
                x = self.war.pop()
                self.lootPile.push(x)
            u_turt.clear()
            Display.user_card_number(self, wn, u_turt, self.myPlayingPile.size())
            x_turt.clear()
            Display.other_card_number(self, wn, x_turt, self.otherPlayingPile.size())
            return self.lootPile

    def move_my_loot(self, wn, t_turt, turt):
        """Moves everything from lootPile to myStoragePile"""
        while self.lootPile.size() != 0:                        # removes all the cards from the lootpile and puts them into the storage pile
            a = self.lootPile.pop()
            self.myStoragePile.enqueue(a)
            Display.user_storage(self, wn, turt)                # displays user storage pile
        t_turt.clear()
        Display.user_storage_number(self, wn, t_turt, self.myStoragePile.size())    # displays number of cards in storage
        return self.myStoragePile

    def move_other_loot(self, wn, o_turt, turt):
        """Moves everything from lootPile to otherStoragePile"""
        while self.lootPile.size() != 0:                        # removes all the cards from the lootpile and puts them into the storage pile
            b = self.lootPile.pop()
            self.otherStoragePile.enqueue(b)
            Display.comp_storage(self, wn, turt)                # displays computer storage pile
        o_turt.clear()
        Display.other_storage_number(self, wn, o_turt, self.otherStoragePile.size())    # displays number of cards in storage
        return self.otherStoragePile

    def move_my_storage(self, wn, u_turt, t_turt, s_turt):
        """Moves everything from myStoragePile to myPlayingPile"""
        if self.myPlayingPile.size() == 0:
            while self.myStoragePile.size() != 0:                   # removes all the cards from the storage pile and puts it into the playing hand
                c = self.myStoragePile.dequeue()
                self.myPlayingPile.push(c)
            if self.myStoragePile.size()== 0:
                return self.myPlayingPile
            else:
                u_turt.clear()
                Display.user_card_number(self, wn, u_turt, self.myPlayingPile.size())   # updated user card number
                Display.replace_card(self, wn, s_turt)                              # moves the storage to the playing pile
                t_turt.clear()
                Display.user_storage_number(self, wn, t_turt, self.myStoragePile.size())    # updates storage pile number
                s_turt.clear()
                return self.myPlayingPile

    def move_other_storage(self, wn, x_turt, o_turt, cs_turt):
        """Moves everything from otherStoragePile to otherPlayingPile"""
        if self.otherPlayingPile.size() == 0:
            while self.otherStoragePile.size() != 0:                # removes all the cards from the storage pile and puts it into the playing hand
                d = self.otherStoragePile.dequeue()
                self.otherPlayingPile.push(d)
            if self.otherStoragePile.size() == 0:
                return self.otherPlayingPile
            else:
                x_turt.clear()
                Display.other_card_number(self, wn, x_turt, self.otherPlayingPile.size())       # updates computer playing pile number
                Display.replace_other_card(self, wn, cs_turt)                                   # moves computer storage to playing pile
                o_turt.clear()
                Display.other_storage_number(self, wn, o_turt, self.otherStoragePile.size())    # updates computer storage pile number
                cs_turt.clear()
                return self.otherPlayingPile
