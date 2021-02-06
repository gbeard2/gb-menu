#
# This file is subject to the terms and conditions defined in
# file 'LICENSE', which is part of this source code package.
#
import gb_menu
import sys
import mock

MAIN_MENU = gb_menu.Menu()
UP_ACTION = None
UP_CHOICE = None
DOWN_ACTION = None
DOWN_CHOICE = None
QUIT_ACTION = None
QUIT_CHOICE = None
X = 0


def increment():
    global X
    X += 1


def decrement():
    global X
    X -= 1


def test_create_action():
    global UP_ACTION, DOWN_ACTION, QUIT_ACTION
    UP_ACTION = gb_menu.Action(function=increment)
    DOWN_ACTION = gb_menu.Action(function=decrement)
    QUIT_ACTION = gb_menu.Action(function=sys.exit)
    assert UP_ACTION.function == increment and DOWN_ACTION.function == decrement and QUIT_ACTION.function == sys.exit


def test_create_choice():
    global UP_CHOICE, DOWN_CHOICE, QUIT_CHOICE
    UP_CHOICE = gb_menu.Choice(key='1', text='X + 1', action=UP_ACTION)
    DOWN_CHOICE = gb_menu.Choice(key='2', text='X - 1', action=DOWN_ACTION)
    QUIT_CHOICE = gb_menu.Choice(key='q', text='Quit', action=QUIT_ACTION)
    assert UP_CHOICE.text == 'X + 1' and DOWN_CHOICE.text == 'X - 1' and QUIT_CHOICE.text == 'Quit'


def test_add_choice():
    global MAIN_MENU
    MAIN_MENU.add_choice(UP_CHOICE)
    MAIN_MENU.add_choice(DOWN_CHOICE)
    MAIN_MENU.add_choice(QUIT_CHOICE)
    assert all(c in MAIN_MENU.choices for c in [UP_CHOICE, DOWN_CHOICE, QUIT_CHOICE])


def test_remove_choice():
    global MAIN_MENU
    MAIN_MENU.remove_choice(UP_CHOICE)
    assert UP_CHOICE not in MAIN_MENU.choices
    MAIN_MENU.add_choice(UP_CHOICE)


def test_increment():
    global MAIN_MENU
    with mock.patch(__builtins__, 'input', lambda: '1'):
        MAIN_MENU.show()
        assert X == 1


def test_decrement():
    global MAIN_MENU
    with mock.patch(__builtins__, 'input', lambda: '2'):
        MAIN_MENU.show()
        assert X == 0
