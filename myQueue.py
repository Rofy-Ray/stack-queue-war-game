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
# Queue.py
# Dave Reed 02/24/2006
#
# from Data Structures and Algorithms Using Python and C++
# downloaded from publisher's website:
# https://www.fbeedle.com/content/data-structures-and-algorithms-using-python-and-c
# on July 23, 2014
########################################################################################################################

#----------------------------------------------------------------------

class Queue:

    #----------------------------------------------------------------------

    def __init__(self):

        '''create an empty FIFO queue'''

        self.q = []

    #----------------------------------------------------------------------

    def size(self):

        '''return number of items in the queue

        pre: none

        post: returns number of items in the queue'''

        return len(self.q)

    #----------------------------------------------------------------------

    def enqueue(self, x):

        '''insert x at end of queue

        pre: none

        post: x is added to the queue'''

        self.q.append(x)

    #----------------------------------------------------------------------

    def front(self):

        '''return first item in queue

        pre: queue is not empty; IndexError is raised if empty

        post: returns first item in the queue'''

        return self.q[0]

    #----------------------------------------------------------------------

    def dequeue(self):

        '''remove and return first item in queue

        pre: queue is not empty; IndexError is raised if empty

        post: removes and returns first item in the queue'''

        return self.q.pop(0)

#----------------------------------------------------------------------
