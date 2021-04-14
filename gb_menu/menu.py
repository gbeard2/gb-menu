#
# This file is subject to the terms and conditions defined in
# file 'LICENSE', which is part of this source code package.
#
from gb_menu.choice import Choice
from gb_menu.textbox import Textbox


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
        self.column_widths = dict()
        self.print_buffer = dict()

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
        self.__add_to_print_buffer__(choice.pos, choice)

    def remove_choice(self, choice):
        del self.choices[choice.key]
        self.style.keys[choice.key] = False
        self.__remove_from_print_buffer__(choice.pos)

    def add_textbox(self, textbox):
        if self.textboxes is None:
            self.textboxes = dict()

        self.textboxes[str(textbox.pos)] = textbox
        self.__add_to_print_buffer__(textbox.pos, textbox)

    def remove_textbox(self, textbox):
        del self.textboxes[textbox.pos]
        self.__remove_from_print_buffer__(textbox.pos)

    def show(self):
        return_values = dict()
        cursor_pos = [1, 1]
        if self.on_show is not None:
            if self.on_show.function is not None:
                return_values['on_show'] = self.on_show.function(**self.on_show.args)

        if self.header is not None:
            print(self.header)

        if self.choices is None:
            raise RuntimeError('Menu must have at least one choice.')
        else:
            while cursor_pos[0] <= self.style.menu_size[0]:
                line = ''
                while cursor_pos[1] <= self.style.menu_size[1]:
                    if cursor_pos[1] > 1:
                        line += self.style.col_spacing + self.style.col_sep + self.style.col_spacing

                    try:
                        item = self.print_buffer[str(cursor_pos)]
                    except KeyError:
                        item = None

                    if isinstance(item, Textbox):
                        text = item.text
                        if len(text) < self.column_widths[cursor_pos[1]]:
                            text += ' ' * (self.column_widths[cursor_pos[1]] - len(text))

                        line += text
                    elif isinstance(item, Choice):
                        text = '{}{}{}'.format(item.key, self.style.key_sep, item.text)
                        if len(text) < self.column_widths[cursor_pos[1]]:
                            text += ' ' * (self.column_widths[cursor_pos[1]] - len(text))

                        line += text
                    elif item is None:
                        line += ' ' * self.column_widths[cursor_pos[1]]
                    else:
                        raise RuntimeError('Unexpected item in print buffer.')

                    cursor_pos[1] += 1
                print(line)
                cursor_pos[0] += 1
                cursor_pos[1] = 1

        sel = input(self.input_text)
        try:
            return_values[self.choices[sel].text] = self.choices[sel].execute()
        except KeyError:
            print(self.invalid_choice_text)
            if self.on_invalid_choice is not None:
                if self.on_invalid_choice.function is not None:
                    return_values['on_invalid_choice'] = self.on_invalid_choice.function(**self.on_show.args)

        if self.textboxes is not None:
            for textbox in self.textboxes.values():
                if textbox.update_on_show:
                    textbox.update()

        return return_values

    def update_column_widths(self):
        self.column_widths = dict()
        for item in self.print_buffer.values():
            if isinstance(item, Textbox):
                try:
                    if self.column_widths[item.pos[1]] < len(item.text):
                        self.column_widths[item.pos[1]] = len(item.text)
                except KeyError:
                    self.column_widths[item.pos[1]] = len(item.text)
            elif isinstance(item, Choice):
                try:
                    if self.column_widths[item.pos[1]] < len(item.key + self.style.key_sep + item.text):
                        self.column_widths[item.pos[1]] = len(item.key + self.style.key_sep + item.text)
                except KeyError:
                    self.column_widths[item.pos[1]] = len(item.key + self.style.key_sep + item.text)

    def __add_to_print_buffer__(self, pos, item):
        if pos > self.style.menu_size:
            raise RuntimeError('Position outside of menu.')

        if isinstance(item, Textbox):
            try:
                if self.column_widths[pos[1]] < len(item.text):
                    self.column_widths[pos[1]] = len(item.text)
            except KeyError:
                self.column_widths[pos[1]] = len(item.text)
        elif isinstance(item, Choice):
            try:
                if self.column_widths[pos[1]] < len(item.key + self.style.key_sep + item.text):
                    self.column_widths[pos[1]] = len(item.key + self.style.key_sep + item.text)
            except KeyError:
                self.column_widths[pos[1]] = len(item.key + self.style.key_sep + item.text)

        pos = str(pos)
        if pos in self.print_buffer:
            if isinstance(self.print_buffer[pos], Choice):
                if isinstance(item, Choice):
                    raise RuntimeError('Choice overlap at position: {}'.format(pos))
                elif isinstance(item, Textbox):
                    raise RuntimeError('Choice and textbox overlap at position: {}'.format(pos))
            elif isinstance(self.print_buffer[pos], Textbox):
                if isinstance(item, Choice):
                    raise RuntimeError('Choice and textbox overlap at position: {}'.format(pos))
                elif isinstance(item, Textbox):
                    raise RuntimeError('Textbox overlap at position: {}'.format(pos))
        else:
            self.print_buffer[pos] = item

    def __remove_from_print_buffer__(self, pos):
        del self.print_buffer[pos]
