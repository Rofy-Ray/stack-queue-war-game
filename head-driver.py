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

import turtle
from war import War
from ply_easygui import play_game

def main():
    turt = turtle.Turtle()                  # turtle objects
    turt.hideturtle()
    o_turt = turtle.Turtle()
    o_turt.hideturtle()
    t_turt = turtle.Turtle()
    t_turt.hideturtle()
    u_turt = turtle.Turtle()
    u_turt.hideturtle()
    x_turt = turtle.Turtle()
    x_turt.hideturtle()
    p_turt = turtle.Turtle()
    p_turt.hideturtle()
    c_turt = turtle.Turtle()
    c_turt.hideturtle()
    c_turt.color('white')
    s_turt = turtle.Turtle()
    s_turt.color('white')
    s_turt.hideturtle()
    cs_turt = turtle.Turtle()
    cs_turt.color('white')
    cs_turt.hideturtle()
    turt.speed(0)
    wn = turtle.Screen()                    # makes screen
    wn.setup(width = 1200, height = 790, startx = None, starty = None)
    wn.bgcolor('turquoise')                 # sets color
    a = War()
    a.add_dealingpile()
    a.deal(wn, turt, u_turt, x_turt)         # deals cards
    play_game()
    while a.make_move(wn, turt) == True:                                        # continues running if there are cards in both hands
        a.remove_my_card()
        a.remove_other_card()
        a.display_card(wn, p_turt, c_turt)
        play_game()
        c = a.compare_cards()
        if c == 0:
            if a.compare_other(wn, u_turt, x_turt) == -1:
                a.remove_my_card()
                a.remove_other_card()
                a.display_card(wn, p_turt, c_turt)
                a.compare_cards()
                a.compare_other(wn, u_turt, x_turt)
            a.move_my_loot(wn, t_turt, turt)
            a.move_my_storage(wn, u_turt, o_turt, s_turt)
            a.move_other_storage(wn, x_turt, t_turt, cs_turt)
        elif c == 1:
            if a.compare_other(wn, u_turt, x_turt) == -1:
                a.remove_my_card()
                a.remove_other_card()
                a.display_card(wn, p_turt, c_turt)
                a.compare_cards()
                a.compare_other(wn, u_turt, x_turt)
            play_game()
            a.move_other_loot(wn, o_turt, turt)
            a.move_other_storage(wn, x_turt, o_turt, s_turt)
            a.move_my_storage(wn, u_turt, t_turt, cs_turt)
    wn.exitonclick()

main()
