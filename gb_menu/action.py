#
# This file is subject to the terms and conditions defined in
# file 'LICENSE', which is part of this source code package.
#
class Action:
    def __init__(self, function, args=None):
        if args is None:
            args = dict()

        self.function = function
        self.args = args
