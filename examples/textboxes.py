#
# This file is subject to the terms and conditions defined in
# file 'LICENSE', which is part of this source code package.
#
from gb_menu import menu, choice, action, style, textbox
import sys
import time

START_TIME = time.time()


def change_name():
    new_name = input('Enter your name: ')
    global name
    name.text = 'Name: ' + new_name


def update_runtime():
    return 'Runtime: ' + str(time.time() - START_TIME) + ' s'


main_menu = menu.Menu(style.DEFAULT)
# Create a textbox to display the user's name
name = textbox.Textbox(text='Name: Unknown', pos=[1, 1])
# Add the textbox to the menu
main_menu.add_textbox(name)
change_name_action = action.Action(function=change_name)
change_name_choice = choice.Choice(text='Change name', action=change_name_action, pos=[2, 1])
main_menu.add_choice(change_name_choice)
quit_action = action.Action(function=sys.exit)
quit_choice = choice.Choice(key='q', text='Quit', action=quit_action, pos=[3, 1])
main_menu.add_choice(quit_choice)

runtime_action = action.Action(function=update_runtime)
# Create a textbox to display the total runtime which updates whenever the menu is displayed
runtime = textbox.Textbox(text='Runtime: 0 s', pos=[5, 1], update_on_show=True, update_action=runtime_action)
main_menu.add_textbox(runtime)

while True:
    main_menu.show()
    print('')
