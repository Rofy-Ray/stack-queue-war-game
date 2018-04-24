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
# Stack.py
#
# by David M. Reed and John Zelle
# from Data Structures and Algorithms Using Python and C++
# downloaded from publisher's website:
# https://www.fbeedle.com/content/data-structures-and-algorithms-using-python-and-c
# on July 23, 2014
########################################################################################################################

class Stack(object):

    #------------------------------------------------------------

    def __init__(self):

        '''post: creates an empty LIFO stack'''

        self.items = []

    #------------------------------------------------------------

    def push(self, item):

        '''post: places x on top of the stack'''

        self.items.append(item)

    #------------------------------------------------------------

    def pop(self):

        '''post: removes and returns the top element of
        the stack'''

        return self.items.pop()

    #------------------------------------------------------------

    def top(self):

        '''post: returns the top element of the stack without
        removing it'''

        return self.items[0]

    #------------------------------------------------------------

    def size(self):

        '''post: returns the number of elements in the stack'''

        return len(self.items)
