#
# This file is subject to the terms and conditions defined in
# file 'LICENSE', which is part of this source code package.
#
from gb_menu import menu, choice, action, style
import sys

X = 0


def increment():
    global X
    X += 1


def decrement():
    global X
    X -= 1


def display():
    global main_menu
    main_menu.header = 'Value of x: {}'.format(X)


# Initialize an empty Menu
main_menu = menu.Menu(style.DEFAULT)

# Create an Action which calls the increment function
up_action = action.Action(function=increment)
# Create a Choice for an input of '1' with the behavior of the above action
up_choice = choice.Choice(text='X + 1', action=up_action)
# Add the Choice to the Menu
main_menu.add_choice(up_choice)

down_action = action.Action(function=decrement)
down_choice = choice.Choice(text='X - 1', action=down_action)
main_menu.add_choice(down_choice)

quit_action = action.Action(function=sys.exit)
quit_choice = choice.Choice(key='q', text='Quit', action=quit_action)
main_menu.add_choice(quit_choice)

# Create an Action to allow the Menu to display the value of X
disp_action = action.Action(function=display)
main_menu.on_show = disp_action

while True:
    main_menu.show()
    print('')
