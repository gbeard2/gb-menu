#
# This file is subject to the terms and conditions defined in
# file 'LICENSE', which is part of this source code package.
#
class Textbox:
    def __init__(self, text, pos=0, update_on_show=False, update_action=None):
        self.text = text
        self.pos = pos
        self.update_on_show = update_on_show
        self.update_action = update_action

    def update(self):
        if self.update_action is not None:
            if self.update_action.function is not None:
                self.text = self.update_action.function(**self.update_action.args)
