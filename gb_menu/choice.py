#
# This file is subject to the terms and conditions defined in
# file 'LICENSE', which is part of this source code package.
#
class Choice:
    def __init__(self, text, key=None, action=None):
        self.key = key
        self.text = text
        self.action = action

    def execute(self):
        if self.action is not None:
            if self.action.function is not None:
                return self.action.function(**self.action.args)
