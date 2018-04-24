########################################################################################################################
# Author: Raymond Okyere-Forson
# Username: okyereforsonr
#
# Assignment: Extra Credit Project - Enhanced Stacks & Queues Card War Game
#
# Purpose: Working with easygui to use stacks and queues in playing the card game.
########################################################################################################################
# Acknowledgements: Aaron Christson & Jamal Aw Yoonis & Saffa Moses Gbondo
#
########################################################################################################################

import easygui as rofy

def play_game():
    x = 0
    play = rofy.ynbox('Continue Play?', 'Stack-Queue War Game', (['PLAY', 'QUIT']))  # brings up a box using easygui and has 2 option for play or quit
    if play == True:               # continues play
        x = 1
    elif play == False:             # quits card game
        quit()
    return x



