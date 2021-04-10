#
# This file is subject to the terms and conditions defined in
# file 'LICENSE', which is part of this source code package.
#
class Menu:
    def __init__(self, style, choices=None, textboxes=None, on_show_action=None, on_invalid_choice_action=None, input_text='Choice: ', invalid_choice_text='Invalid input.'):
        self.style = style
        self.header = style.header
        self.choices = choices
        self.textboxes = textboxes
        self.textbox_count = textboxes.size() if self.textboxes is not None else 0
        self.on_show = on_show_action
        self.on_invalid_choice = on_invalid_choice_action
        self.key_sep = style.key_sep
        self.input_text = input_text
        self.invalid_choice_text = invalid_choice_text
        self.cursor_pos = -1

    def add_choice(self, choice):
        if self.choices is None:
            self.choices = dict()

        # TODO: Optimize ... find first key with value of false
        if choice.key is None:
            found = False
            for key, value in self.style.keys.items():
                if not value:
                    choice.key = key
                    found = True
                    break
            if not found:
                raise RuntimeError('Not enough keys available to add choice.')

        self.choices[choice.key] = choice
        self.style.keys[choice.key] = True

    def remove_choice(self, choice):
        del self.choices[choice.key]
        self.style.keys[choice.key] = False

    def add_textbox(self, textbox):
        if self.textboxes is None:
            self.textboxes = dict()

        invalid_pos = True
        while invalid_pos:
            if textbox.pos in self.textboxes:
                textbox.pos += 1
            else:
                self.textboxes[textbox.pos] = textbox
                self.textbox_count += 1
                invalid_pos = False

    def remove_textbox(self, textbox):
        del self.textboxes[textbox.pos]
        self.textboxes -= 1

    def show(self):
        self.cursor_pos = 0
        if self.on_show is not None:
            if self.on_show.function is not None:
                self.on_show.function(**self.on_show.args)

        if self.header is not None:
            print(self.header)

        if self.choices is None:
            raise RuntimeError('Menu must have at least one choice.')
        else:
            if self.textboxes is not None:
                textboxes_displayed = 0
                for key, choice in self.choices.items():
                    textbox_available = self.cursor_pos in self.textboxes
                    while textbox_available:
                        print(self.textboxes[self.cursor_pos].text)
                        textboxes_displayed += 1
                        self.cursor_pos += 1
                        textbox_available = self.cursor_pos in self.textboxes
                    print('{}{}{}'.format(choice.key, self.key_sep, choice.text))
                    self.cursor_pos += 1
                while textboxes_displayed < self.textbox_count:
                    try:
                        print(self.textboxes[self.cursor_pos].text)
                        textboxes_displayed += 1
                    except KeyError:
                        print('')
                    finally:
                        self.cursor_pos += 1
            else:
                for key, choice in self.choices.items():
                    print('{}{}{}'.format(choice.key, self.key_sep, choice.text))
                    self.cursor_pos += 1

        sel = input(self.input_text)
        try:
            self.choices[sel].execute()
        except KeyError:
            print(self.invalid_choice_text)
            if self.on_invalid_choice is not None:
                if self.on_invalid_choice.function is not None:
                    self.on_invalid_choice.function(**self.on_show.args)

        if self.textboxes is not None:
            for textbox in self.textboxes.values():
                if textbox.update_on_show:
                    textbox.update()
