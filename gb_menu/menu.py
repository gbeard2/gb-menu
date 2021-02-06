#
# This file is subject to the terms and conditions defined in
# file 'LICENSE', which is part of this source code package.
#
class Menu:
    def __init__(self, header=None, choices=None, on_show=None, on_invalid_choice=None, key_sep=': ', input_text='Choice: ', invalid_choice_text='Invalid input.'):
        self.header = header
        self.choices = choices
        self.on_show = on_show
        self.on_invalid_choice = on_invalid_choice
        self.key_sep = key_sep
        self.input_text = input_text
        self.invalid_choice_text = invalid_choice_text

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
        try:
            self.choices[sel].execute()
        except KeyError:
            print(self.invalid_choice_text)
            if self.on_invalid_choice is not None:
                self.on_invalid_choice.function(**self.on_show.args)
