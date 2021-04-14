#
# This file is subject to the terms and conditions defined in
# file 'LICENSE', which is part of this source code package.
#
from gb_menu import menu, choice, action, style, textbox
import sys

main_menu = menu.Menu(style.DEFAULT)
# Set menu size to 3 rows, 3 columns
main_menu.style.menu_size = [3, 3]

name = textbox.Textbox(text='Garrett', pos=[1, 1])
main_menu.add_textbox(name)

date = textbox.Textbox(text='4/14/2021', pos=[1, 2])
main_menu.add_textbox(date)

version = textbox.Textbox(text='Python 3.9', pos=[1, 3])
main_menu.add_textbox(version)

change_name_action = action.Action(function=input, args={'__prompt': 'Name: '})
change_name_choice = choice.Choice(text='Change name', pos=[2, 1], action=change_name_action)
main_menu.add_choice(change_name_choice)

change_date_action = action.Action(function=input, args={'__prompt': 'Date: '})
change_date_choice = choice.Choice(text='Change date', pos=[2, 2], action=change_date_action)
main_menu.add_choice(change_date_choice)

change_version_action = action.Action(function=input, args={'__prompt': 'Version: '})
change_version_choice = choice.Choice(text='Change version', pos=[2, 3], action=change_version_action)
main_menu.add_choice(change_version_choice)

quit_action = action.Action(function=sys.exit)
quit_choice = choice.Choice(key='q', text='Quit', action=quit_action, pos=[3, 1])
main_menu.add_choice(quit_choice)

while True:
    return_values = main_menu.show()

    try:
        name.text = return_values['Change name']
    except KeyError:
        try:
            date.text = return_values['Change date']
        except KeyError:
            try:
                version.text = return_values['Change version']
            except KeyError:
                pass

    main_menu.update_column_widths()
    print('')
