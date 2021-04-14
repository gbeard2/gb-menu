#
# This file is subject to the terms and conditions defined in
# file 'LICENSE', which is part of this source code package.
#
from gb_menu import menu, choice, action, style
import sys
import random

main_menu = menu.Menu(style.DEFAULT)
gen_random_action = action.Action(function=random.randint, args={'a': 0, 'b': 10})
gen_random_choice = choice.Choice(text='Generate random number', action=gen_random_action, pos=[1, 1])
main_menu.add_choice(gen_random_choice)

quit_action = action.Action(function=sys.exit)
quit_choice = choice.Choice(key='q', text='Quit', action=quit_action, pos=[2, 1])
main_menu.add_choice(quit_choice)


while True:
    return_values = main_menu.show()
    # Add the output of random.randint to the header, accessed via the choice text
    main_menu.header = 'Random number: ' + str(return_values['Generate random number'])
    print('')
