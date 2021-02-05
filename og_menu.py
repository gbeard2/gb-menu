#
# This file is subject to the terms and conditions defined in
# file 'LICENSE.txt', which is part of this source code package.
#
class Action:
    def __init__(self, function, args=None):
        if args is None:
            args = dict()

        self.function = function
        self.args = args


class Choice:
    def __init__(self, key, text, action=None):
        self.key = key
        self.text = text
        self.action = action

    def execute(self):
        self.action.function(**self.action.args)


class Menu:
    def __init__(self, header=None, choices=None, on_show=None, key_sep=': ', input_text='Choice: '):
        self.header = header
        self.choices = choices
        self.on_show = on_show
        self.key_sep = key_sep
        self.input_text = input_text

    def add_choice(self, choice):
        if self.choices is None:
            self.choices = dict()

        self.choices[choice.key] = choice

    def remove_choice(self, choice):
        del self.choices[choice.key]

    def show(self):
        if self.on_show is not None:
            self.on_show.function(**self.on_show.args)

        if self.header is not None:
            print(self.header)

        if self.choices is None:
            raise RuntimeError('Menu must have at least one choice.')
        else:
            for key, choice in self.choices.items():
                print('{}{}{}'.format(choice.key, self.key_sep, choice.text))

        sel = input(self.input_text)
        self.choices[sel].execute()