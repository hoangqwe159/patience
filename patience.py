
#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item.  By submitting this
#  code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#    Student no: 10329935
#    Student name: DO VIET HOANG
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  All files submitted will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#



#-----Assignment Description-----------------------------------------#
#
# PATIENCE
#
# This assignment tests your skills at processing data stored in
# lists, creating reusable code and following instructions to display
# a complex visual image.  The incomplete Python program below is
# missing a crucial function, "deal_cards".  You are required to
# complete this function so that when the program is run it draws a
# game of Patience (also called Solitaire in the US), consisting of
# multiple stacks of cards in four suits.  See the instruction sheet
# accompanying this file for full details.
#
# Note that this assignment is in two parts, the second of which
# will be released only just before the final deadline.  This
# template file will be used for both parts and you will submit
# your final solution as a single Python 3 file, whether or not you
# complete both parts of the assignment.
#
#--------------------------------------------------------------------#  



#-----Preamble-------------------------------------------------------#
#
# This section imports necessary functions and defines constant
# values used for creating the drawing canvas.  You should not change
# any of the code in this section.
#

# Import the functions needed to complete this assignment.  You
# should not need to use any other modules for your solution.  In
# particular, your solution must NOT rely on any non-standard Python
# modules that need to be installed separately, because the markers
# will not have access to such modules.

from turtle import *
from math import *
from random import *

# Define constant values used in the main program that sets up
# the drawing canvas.  Do not change any of these values.

# Constants defining the size of the card table
table_width = 1100 # width of the card table in pixels
table_height = 800 # height (actually depth) of the card table in pixels
canvas_border = 30 # border between playing area and window's edge in pixels
half_width = table_width // 2 # maximum x coordinate on table in either direction
half_height = table_height // 2 # maximum y coordinate on table in either direction

# Work out how wide some text is (in pixels)
def calculate_text_width(string, text_font = None):
    penup()
    home()
    write(string, align = 'left', move = True, font = text_font)
    text_width = xcor()
    undo() # write
    undo() # goto
    undo() # penup
    return text_width

# Constants used for drawing the coordinate axes
axis_font = ('Consolas', 10, 'normal') # font for drawing the axes
font_height = 14 # interline separation for text
tic_sep = 50 # gradations for the x and y scales shown on the screen
tics_width = calculate_text_width("-mmm -", axis_font) # width of y axis labels

# Constants defining the stacks of cards
stack_base = half_height - 25 # starting y coordinate for the stacks
num_stacks = 6 # how many locations there are for the stacks
stack_width = table_width / (num_stacks + 1) # max width of stacks
stack_gap = (table_width - num_stacks * stack_width) // (num_stacks + 1) # inter-stack gap
max_cards = 10 # maximum number of cards per stack

# Define the starting locations of each stack
stack_locations = [["Stack " + str(loc + 1),
                    [int(-half_width + (loc + 1) * stack_gap + loc * stack_width + stack_width / 2),
                     stack_base]] 
                    for loc in range(num_stacks)]

# Same as Turtle's write command, but writes upside down
def write_upside_down(string, **named_params):
    named_params['angle'] = 180
    tk_canvas = getscreen().cv
    tk_canvas.create_text(xcor(), -ycor(), named_params, text = string)

#
#--------------------------------------------------------------------#



#-----Functions for Creating the Drawing Canvas----------------------#
#
# The functions in this section are called by the main program to
# create the drawing canvas for your image.  You should not change
# any of the code in this section.
#

# Set up the canvas and draw the background for the overall image.
# By default the coordinate axes displayed - call the function
# with False as the argument to prevent this.
def create_drawing_canvas(show_axes = True):

    # Set up the drawing canvas
    setup(table_width + tics_width + canvas_border * 2,
          table_height + font_height + canvas_border * 2)

    # Draw as fast as possible
    tracer(False)

    # Make the background felt green and the pen a lighter colour
    bgcolor('green')
    pencolor('light green')

    # Lift the pen while drawing the axes
    penup()

    # Optionally draw x coordinates along the bottom of the table
    if show_axes:
        for x_coord in range(-half_width + tic_sep, half_width, tic_sep):
            goto(x_coord, -half_height - font_height)
            write('| ' + str(x_coord), align = 'left', font = axis_font)

    # Optionally draw y coordinates to the left of the table
    if show_axes:
        max_tic = int(stack_base / tic_sep) * tic_sep
        for y_coord in range(-max_tic, max_tic + tic_sep, tic_sep):
            goto(-half_width, y_coord - font_height / 2)
            write(str(y_coord).rjust(4) + ' -', font = axis_font, align = 'right')

    # Optionally mark each of the starting points for the stacks
    if show_axes:
        for name, location in stack_locations:
            # Draw the central dot
            goto(location)
            color('light green')
            dot(7)
            # Draw the horizontal line
            pensize(2)
            goto(location[0] - (stack_width // 2), location[1])
            setheading(0)
            pendown()
            forward(stack_width)
            penup()
            goto(location[0] -  (stack_width // 2), location[1] + 4)
            # Write the coordinate
            write(name + ': ' + str(location), font = axis_font)

    #Draw a border around the entire table
    penup()
    pensize(3)
    goto(-half_width, half_height) # top left
    pendown()
    goto(half_width, half_height) # top
    goto(half_width, -half_height) # right
    goto(-half_width, -half_height) # bottom
    goto(-half_width, half_height) # left

    # Reset everything, ready for the student's solution
    pencolor('black')
    width(1)
    penup()
    home()
    tracer(True)


# End the program and release the drawing canvas.
# By default the cursor (turtle) is hidden when the program
# ends - call the function with False as the argument to
# prevent this.
def release_drawing_canvas(hide_cursor = True):
    tracer(True) # ensure any partial drawing in progress is displayed
    if hide_cursor:
        hideturtle()
    done()
    
#
#--------------------------------------------------------------------#



#-----Test Data for Use During Code Development----------------------#
#
# The "fixed" data sets in this section are provided to help you
# develop and test your code.  You can use them as the argument to
# the deal_cards function while perfecting your solution.  However,
# they will NOT be used to assess your program.  Your solution will
# be assessed using the random_game function appearing below.  Your
# program must work correctly for any data set that can be generated
# by the random_game function.
#

# Each of these fixed games draws just one card
fixed_game_0 = [['Stack 1', 'Suit A', 1, 0]]
fixed_game_1 = [['Stack 2', 'Suit B', 1, 0]]
fixed_game_2 = [['Stack 3', 'Suit C', 1, 0]]
fixed_game_3 = [['Stack 4', 'Suit D', 1, 0]]

# Each of these fixed games draws several copies of just one card
fixed_game_4 = [['Stack 2', 'Suit A', 4, 0]]
fixed_game_5 = [['Stack 3', 'Suit B', 3, 0]]
fixed_game_6 = [['Stack 4', 'Suit C', 2, 0]]
fixed_game_7 = [['Stack 5', 'Suit D', 5, 0]]

# This fixed game draws each of the four cards once
fixed_game_8 = [['Stack 1', 'Suit A', 1, 0],
                ['Stack 2', 'Suit B', 1, 0],
                ['Stack 3', 'Suit C', 1, 0],
                ['Stack 4', 'Suit D', 1, 0]]

# These fixed games each contain a non-zero "extra" value
fixed_game_9 = [['Stack 3', 'Suit D', 4, 4]]
fixed_game_10 = [['Stack 4', 'Suit C', 3, 2]]
fixed_game_11 = [['Stack 5', 'Suit B', 2, 1]]
fixed_game_12 = [['Stack 6', 'Suit A', 5, 5]]

# These fixed games describe some "typical" layouts with multiple
# cards and suits. You can create more such data sets yourself
# by calling function random_game in the shell window

fixed_game_13 = \
 [['Stack 6', 'Suit D', 9, 6],
  ['Stack 4', 'Suit B', 5, 0],
  ['Stack 5', 'Suit B', 1, 1],
  ['Stack 2', 'Suit C', 4, 0]]
 
fixed_game_14 = \
 [['Stack 1', 'Suit C', 1, 0],
  ['Stack 5', 'Suit D', 2, 1],
  ['Stack 3', 'Suit A', 2, 0],
  ['Stack 2', 'Suit A', 8, 5],
  ['Stack 6', 'Suit C', 10, 0]]

fixed_game_15 = \
 [['Stack 3', 'Suit D', 0, 0],
  ['Stack 6', 'Suit B', 2, 0],
  ['Stack 2', 'Suit D', 6, 0],
  ['Stack 1', 'Suit C', 1, 0],
  ['Stack 4', 'Suit B', 1, 1],
  ['Stack 5', 'Suit A', 3, 0]]

fixed_game_16 = \
 [['Stack 6', 'Suit C', 8, 0],
  ['Stack 2', 'Suit C', 4, 4],
  ['Stack 5', 'Suit A', 9, 3],
  ['Stack 4', 'Suit C', 0, 0],
  ['Stack 1', 'Suit A', 5, 0],
  ['Stack 3', 'Suit B', 5, 0]]

fixed_game_17 = \
 [['Stack 4', 'Suit A', 6, 0],
  ['Stack 6', 'Suit C', 1, 1],
  ['Stack 5', 'Suit C', 4, 0],
  ['Stack 1', 'Suit D', 10, 0],
  ['Stack 3', 'Suit B', 9, 0],
  ['Stack 2', 'Suit D', 2, 2]]
 
# The "full_game" dataset describes a random game
# containing the maximum number of cards
stacks = ['Stack ' + str(stack_num+1) for stack_num in range(num_stacks)]
shuffle(stacks)
suits = ['Suit ' + chr(ord('A')+suit_num) for suit_num in range(4)]
shuffle(suits)
full_game = [[stacks[stack], suits[stack % 4], max_cards, randint(0, max_cards)]
             for stack in range(num_stacks)]


#
#--------------------------------------------------------------------#



#-----Function for Assessing Your Solution---------------------------#
#
# The function in this section will be used to mark your solution.
# Do not change any of the code in this section.
#
# The following function creates a random data set specifying a game
# of Patience to be drawn.  Your program must work for any data set 
# returned by this function.  The results returned by calling this 
# function will be used as the argument to your deal_cards function 
# during marking. For convenience during code development and marking 
# this function also prints the game data to the shell window.
#
# Each of the data sets generated is a list specifying a set of
# card stacks to be drawn. Each specification consists of the
# following parts:
#
# a) Which stack is being described, from Stack 1 to num_stacks.
# b) The suit of cards in the stack, from 'A' to 'D'.
# c) The number of cards in the stack, from 0 to max_cards
# d) An "extra" value, from 0 to max_cards, whose purpose will be
#    revealed only in Part B of the assignment.  You should
#    ignore it while completing Part A.
#
# There will be up to num_stacks specifications, but sometimes fewer
# stacks will be described, so your code must work for any number
# of stack specifications.
#
def random_game(print_game = True):

    # Percent chance of the extra value being non-zero
    extra_probability = 20

    # Generate all the stack and suit names playable
    game_stacks = ['Stack ' + str(stack_num+1)
                   for stack_num in range(num_stacks)]
    game_suits = ['Suit ' + chr(ord('A')+suit_num)
                  for suit_num in range(4)]

    # Create a list of stack specifications
    game = []

    # Randomly order the stacks
    shuffle(game_stacks)

    # Create the individual stack specifications 
    for stack in game_stacks:
        # Choose the suit and number of cards
        suit = choice(game_suits)
        num_cards = randint(0, max_cards)
        # Choose the extra value
        if num_cards > 0 and randint(1, 100) <= extra_probability: 
            option = randint(1,num_cards)
        else:
            option = 0
        # Add the stack to the game, but if the number of cards
        # is zero we will usually choose to omit it entirely
        if num_cards != 0 or randint(1, 4) == 4:
            game.append([stack, suit, num_cards, option])
        
    # Optionally print the result to the shell window
    if print_game:
        print('\nCards to draw ' +
              '(stack, suit, no. cards, option):\n\n',
              str(game).replace('],', '],\n '))
    
    # Return the result to the student's deal_cards function
    return game

#
#--------------------------------------------------------------------#



#-----Student's Solution---------------------------------------------#
#
#  Complete the assignment by replacing the dummy function below with
#  your own "deal_cards" function.
#

# Draw the card stacks as per the provided game specification

#The location of 6 stacks
stack = {
    'Stack 1': [-449, 350],
    'Stack 2': [-270, 350],
    'Stack 3': [- 91, 350],
    'Stack 4': [  88, 350],
    'Stack 5': [ 267, 350],
    'Stack 6': [ 446, 350]
}
index_card = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
card_width = 150
card_heigth = 200
card_step = 50

#Color set
white = '#ffffff'
light_yellow = '#eaea88'
brown = "#B69200"
green = "#00B63D"
light_blue = '#42d6ff'
pink = '#ff21cb'



def draw_index(x, y, index):
    # x and y are coordinates of the cards
    # index is the number of the card A, K, Q, J ,10, ...
    c = getcanvas()
    index_bottom = c.create_text(x + card_width * 0.4, - y + card_heigth * 0.9, text=str(index), angle=180, font=("Comic Sans MS", 12, "normal"))
    index_top = c.create_text(x - card_width * 0.4, - y + card_heigth * 0.1, text= str(index), font=("Comic Sans MS", 12, "normal"))

def rounded_rectangle(x, y, long = card_heigth, short = card_width, radius = 16,  colour = white):
    pensize(0)
    pencolor(colour)
    diameter = radius * 2
    fillcolor(colour)
    setheading(270)
    penup()
    goto(x - short/2, y - long + radius)
    pendown()
    begin_fill()

    for _ in range(2):
        circle(radius, 90)
        forward(short - diameter)
        circle(radius, 90)
        forward(long - diameter)

    end_fill()
    penup()
    goto(x, y - long/2)

def draw_petal_A(radius):
    fillcolor('yellow')
    begin_fill()
    angle = heading()
    circle(radius, 60)
    left(120)
    circle(radius, 60)
    setheading(angle)
    end_fill()

def draw_flower_A():
    #Draw flower for card in Suit A
    pendown()
    pencolor('yellow')
    pentals = 10
    flower_radius = 75
    for curves in range(pentals * 2):
        draw_petal_A(flower_radius)
        left(360 / pentals)

    pencolor(light_yellow)
    pensize(2)
    for curves in range(pentals):
        draw_petal_A(flower_radius)
        left(360 / pentals)
    pencolor('red')
    dot(9)
    penup()

def draw_suit_A(x, y, index):
    #Draw a card with 2 rounded rectangles
    rounded_rectangle(x, y)
    rounded_rectangle(x, y - 3, 194, 144, 14, light_yellow)

    #Draw flower A
    draw_flower_A()

    #Draw index of the card
    draw_index(x, y, index)

def draw_flower_B(radius):
    pendown()
    length = radius / sqrt(3)
    colours = ["cyan", "purple", "white", "blue"]
    for number_pentals in range(10):
        colour = choice(colours)
        pensize(2)
        pencolor(light_yellow)
        fillcolor(colour)
        begin_fill()
        for i in range(2):
            forward(length)
            right(60)
            forward(length)
            right(120)
        end_fill()
        right(36)
    dot(9)
    pendown()

def draw_suit_B(x, y, index):
    # Draw a card with 2 rounded rectangles
    rounded_rectangle(x, y)
    rounded_rectangle(x, y - 3, 194, 144, 14, light_yellow)

    draw_flower_B(75)
    draw_index(x, y, index)

def draw_petal_C(radius, angle):
    # Draws a petal with two arcs.
    for i in range(2):
        # Draws an arc with the given radius and angle.
        arc_length = 2 * pi * radius * angle / 360
        n = arc_length // 4 + 1
        step_angle = angle / n
        left(step_angle / 2)
        pendown()
        circle(radius, extent=angle)
        right(step_angle / 2)
        left(180 - angle)

def draw_flower_C(pental_number, arc_radius, angle):
    pencolor(pink)
    width(3)
    for i in range(pental_number):
        draw_petal_C(arc_radius, angle)
        left(360 / pental_number)
    pendown()

    pencolor('green')
    dot(20)
    pencolor('yellow')
    dot(15)
    penup()

def draw_suit_C(x, y, index):
    rounded_rectangle(x, y)
    rounded_rectangle(x, y - 3, 194, 144, 14, light_yellow)

    draw_flower_C(15, 40, 120)
    draw_index(x, y, index)

def draw_petal_D(radius, r, g, b):
    colormode(255)
    color(r, g, b)
    begin_fill()
    for angle_step in range(360):
        length = (90 - abs(90 - float(angle_step % 180))) / radius
        forward(length)
        right(1)
    end_fill()

def draw_flower_D(pental_number):
    pendown()
    for index_pental in range(pental_number):
        r = 255
        g = randint(0, 150)
        b = randint(0, 150)
        draw_petal_D(100, r, g, b)
        left(360 / pental_number)
    pencolor('yellow')
    dot(10)
    penup()

def draw_suit_D(x, y, index):
    rounded_rectangle(x, y)
    rounded_rectangle(x, y - 3, 194, 144, 14, light_yellow)
    draw_flower_D(9)
    draw_index(x, y, index)

def draw_branch_joker(pen_size, length, layer):
    if layer >= 3:
        pencolor(green)
        pensize(pen_size)
    else:
        pensize(pen_size * 1.3)
        pencolor(brown)

    pendown()
    forward(length)
    penup()

    if layer < 5:

        side_branch_angle = 33
        middle_branch_angle = randint(-10, 10)

        #draw left side branch
        left(side_branch_angle)
        draw_branch_joker(floor(pen_size * .75), floor(length * .67), layer + 1)
        backward(floor(length * .67))
        right(side_branch_angle)

        # draw middle branch
        right(middle_branch_angle)
        draw_branch_joker(floor(pen_size * .75), floor(length * .67), layer + 1)
        backward(floor(length * .67))
        left(middle_branch_angle)

        # draw right side branch
        right(side_branch_angle)
        draw_branch_joker(floor(pen_size * .67), floor(length * .67), layer + 1)
        backward(floor(length * .67))
        left(side_branch_angle)

def draw_tree_joker(x, y, size, length, depth):
    setheading(90)
    penup()
    goto(x, y)
    pendown()
    draw_branch_joker(size, length, depth)

def draw_joker(x, y):
    rounded_rectangle(x, y)
    rounded_rectangle(x, y - 3, 194, 144, 14, light_blue)
    draw_tree_joker(x, y - 165, 7, 55, 0)

def deal_cards(game):
    global stack, index_card, card_step
    for stacks in range(len(game)):
        #the index of the first card in the stack
        card_number = randint(0, len(index_card) - game[stacks][2])

        #Coordinates of stack
        x = stack[game[stacks][0]][0]
        y = stack[game[stacks][0]][1]

        for card in range(game[stacks][2]):
            if card != (game[stacks][3] - 1):
                if game[stacks][1] == 'Suit A':
                    draw_suit_A(x, y - card_step * card, index_card[card_number])
                elif game[stacks][1] == 'Suit B':
                    draw_suit_B(x, y - card_step * card, index_card[card_number])
                elif game[stacks][1] == 'Suit C':
                    draw_suit_C(x, y - card_step * card, index_card[card_number])
                elif game[stacks][1] == 'Suit D':
                    draw_suit_D(x, y - card_step * card, index_card[card_number])
            else:
                draw_joker(x, y - card_step * card)
            card_number += 1






#--------------------------------------------------------------------#



#-----Main Program---------------------------------------------------#
#
# This main program sets up the background, ready for you to start
# drawing the card game.  Do not change any of this code except
# as indicated by the comments marked '*****'.
#

# Set up the drawing canvas
# ***** Change the default argument to False if you don't want to
# ***** display the coordinates and stack locations
create_drawing_canvas()

# Control the drawing speed
# ***** Modify the following argument if you want to adjust
# ***** the drawing speed
speed('fastest')

# Decide whether or not to show the drawing being done step-by-step
# ***** Set the following argument to False if you don't want to wait
# ***** while the cursor moves around the screen
tracer(False)

# Give the drawing canvas a title
# ***** Replace this title with a description of your cards' theme
title("Flowers")

### Call the student's function to draw the game
### ***** While developing your program you can call the deal_cards
### ***** function with one of the "fixed" data sets, but your
### ***** final solution must work with "random_game()" as the
### ***** argument to the deal_cards function.  Your program must
### ***** work for any data set that can be returned by the
### ***** random_game function.
# deal_cards(fixed_game_0) # <-- used for code development only, not marking
#deal_cards(full_game) # <-- used for code development only, not marking

deal_cards(random_game()) # <-- used for assessment

# Exit gracefully
# ***** Change the default argument to False if you want the
# ***** cursor (turtle) to remain visible at the end of the
# ***** program as a debugging aid
release_drawing_canvas()

#
#--------------------------------------------------------------------#

