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
import random


class Deck:

    def __init__(self):
        self.cards = Stack()
        self.build()

    def build(self):                # This is method creates the deck of cards that we are dealing in the game
        for i in range(2):
            for v in range(0, 10):   # We have 20 cards here
                self.cards.push(v)
        return self.cards

    def shuffle(self):              # This method takes the numbers of cards and randomly shuffle them
        shuffled_deck = []

        for card in range(self.cards.size()):
            shuffled_deck.append(self.cards.pop())

        for i in range(len(shuffled_deck)-1,0,-1):
            r = random.randint(0,i)
            shuffled_deck[i], shuffled_deck[r] = shuffled_deck[r], shuffled_deck[i]

        for card in shuffled_deck:
            self.cards.push(card)

        return self.cards

