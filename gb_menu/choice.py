#
# This file is subject to the terms and conditions defined in
# file 'LICENSE', which is part of this source code package.
#
class Choice:
    def __init__(self, key, text, action=None):
        self.key = key
        self.text = text
        self.action = action

    def execute(self):
        self.action.function(**self.action.args)
