#
# This file is subject to the terms and conditions defined in
# file 'LICENSE', which is part of this source code package.
#
from gb_menu import menu, choice, action, style
import time
import sys

TIME = time.localtime()
SHOW_WEEKDAY = True
SHOW_MONTH = True
SHOW_DAY = True
SHOW_YEAR = True
SHOW_HOURS = True
SHOW_MINUTES = True
SHOW_SECONDS = True

int_to_weekday = {0: 'Mon', 1: 'Tues', 2: 'Wed', 3: 'Thurs', 4: 'Fri', 5: 'Sat', 6: 'Sun'}
int_to_month = {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun', 7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'}


def update_time():
    global TIME
    TIME = time.localtime()


def toggle_weekday():
    global SHOW_WEEKDAY
    SHOW_WEEKDAY = not SHOW_WEEKDAY


def toggle_month():
    global SHOW_MONTH
    SHOW_MONTH = not SHOW_MONTH


def toggle_day():
    global SHOW_DAY
    SHOW_DAY = not SHOW_DAY


def toggle_year():
    global SHOW_YEAR
    SHOW_YEAR = not SHOW_YEAR


def toggle_hours():
    global SHOW_HOURS
    SHOW_HOURS = not SHOW_HOURS


def toggle_minutes():
    global SHOW_MINUTES
    SHOW_MINUTES = not SHOW_MINUTES


def toggle_seconds():
    global SHOW_SECONDS
    SHOW_SECONDS = not SHOW_SECONDS


def update_choices():
    """Function to update the text of each choice to display its current value"""
    global util_menu
    for c in util_menu.choices.values():
        if c.text.find('weekday') != -1:
            c.text = 'Toggle weekday [{}]'.format(SHOW_WEEKDAY)
        elif c.text.find('month') != -1:
            c.text = 'Toggle month [{}]'.format(SHOW_MONTH)
        elif c.text.find('day') != -1:
            c.text = 'Toggle day [{}]'.format(SHOW_DAY)
        elif c.text.find('year') != -1:
            c.text = 'Toggle year [{}]'.format(SHOW_YEAR)
        elif c.text.find('hours') != -1:
            c.text = 'Toggle hours [{}]'.format(SHOW_HOURS)
        elif c.text.find('minutes') != -1:
            c.text = 'Toggle minutes [{}]'.format(SHOW_MINUTES)
        elif c.text.find('seconds') != -1:
            c.text = 'Toggle seconds [{}]'.format(SHOW_SECONDS)


def display():
    global main_menu
    main_menu.header = 'Current time: '
    if SHOW_WEEKDAY:
        main_menu.header += int_to_weekday[TIME.tm_wday] + ' '
    if SHOW_MONTH:
        main_menu.header += int_to_month[TIME.tm_mon] + ' '
    if SHOW_DAY:
        main_menu.header += str(TIME.tm_mday) + ' '
    if SHOW_YEAR:
        main_menu.header += str(TIME.tm_year) + ' '
    if SHOW_HOURS:
        main_menu.header += str(TIME.tm_hour) + ':'
    if SHOW_MINUTES:
        main_menu.header += str(TIME.tm_min) + '::'
    if SHOW_SECONDS:
        main_menu.header += str(TIME.tm_sec) + ' '
    else:
        main_menu.header = main_menu.header.strip('::')
    main_menu.header = main_menu.header.strip()


main_menu = menu.Menu(style.DEFAULT)
# Create a second menu, this will be nested in the main menu
util_menu = menu.Menu(style.Style(header='\nUtilities'))
util_menu.style.menu_size = [8, 1]

# See examples/up_down.py for a description of creating choices and actions
update_action = action.Action(function=update_time)
update_choice = choice.Choice(text='Update time', action=update_action, pos=[1, 1])
main_menu.add_choice(update_choice)

# Setting the function as another menu's show function is how menus can be "nested"
switch_menu_action = action.Action(function=util_menu.show)
switch_menu_choice = choice.Choice(text='Utilities', action=switch_menu_action, pos=[2, 1])
main_menu.add_choice(switch_menu_choice)

quit_action = action.Action(function=sys.exit)
quit_choice = choice.Choice(key='q', text='Quit', action=quit_action, pos=[3, 1])
main_menu.add_choice(quit_choice)

disp_action = action.Action(function=display)
main_menu.on_show = disp_action

toggle_weekday_action = action.Action(function=toggle_weekday)
toggle_weekday_choice = choice.Choice(text='Toggle weekday [{}]'.format(SHOW_WEEKDAY), action=toggle_weekday_action, pos=[1, 1])
util_menu.add_choice(toggle_weekday_choice)

toggle_month_action = action.Action(function=toggle_month)
toggle_month_choice = choice.Choice(text='Toggle month [{}]'.format(SHOW_MONTH), action=toggle_month_action, pos=[2, 1])
util_menu.add_choice(toggle_month_choice)

toggle_day_action = action.Action(function=toggle_day)
toggle_day_choice = choice.Choice(text='Toggle day [{}]'.format(SHOW_DAY), action=toggle_day_action, pos=[3, 1])
util_menu.add_choice(toggle_day_choice)

toggle_year_action = action.Action(function=toggle_year)
toggle_year_choice = choice.Choice(text='Toggle year [{}]'.format(SHOW_YEAR), action=toggle_year_action, pos=[4, 1])
util_menu.add_choice(toggle_year_choice)

toggle_hours_action = action.Action(function=toggle_hours)
toggle_hours_choice = choice.Choice(text='Toggle hours [{}]'.format(SHOW_HOURS), action=toggle_hours_action, pos=[5, 1])
util_menu.add_choice(toggle_hours_choice)

toggle_minutes_action = action.Action(function=toggle_minutes)
toggle_minutes_choice = choice.Choice(text='Toggle minutes [{}]'.format(SHOW_MINUTES), action=toggle_minutes_action, pos=[6, 1])
util_menu.add_choice(toggle_minutes_choice)

toggle_seconds_action = action.Action(function=toggle_seconds)
toggle_seconds_choice = choice.Choice(text='Toggle seconds [{}]'.format(SHOW_SECONDS), action=toggle_seconds_action, pos=[7, 1])
util_menu.add_choice(toggle_seconds_choice)

cancel_choice = choice.Choice(text='Cancel', pos=[8, 1])
util_menu.add_choice(cancel_choice)

update_choices_action = action.Action(function=update_choices)
util_menu.on_show = update_choices_action

# Since the util menu is not in a loop, set the on_invalid_choice action to show the menu again
invalid_input_action = action.Action(function=util_menu.show)
util_menu.on_invalid_choice = invalid_input_action

while True:
    main_menu.show()
    print('')
