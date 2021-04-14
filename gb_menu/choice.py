#
# This file is subject to the terms and conditions defined in
# file 'LICENSE', which is part of this source code package.
#
class Choice:
    def __init__(self, text, pos, key=None, action=None):
        self.key = key
        self.pos = pos
        self.text = text
        self.action = action

    def execute(self):
        if self.action is not None:
            if self.action.function is not None:
                if self.action.function == input:
                    return self.action.function(self.action.args['__prompt'])
                else:
                    return self.action.function(**self.action.args)
