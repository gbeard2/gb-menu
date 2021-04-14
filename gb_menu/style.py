#
# This file is subject to the terms and conditions defined in
# file 'LICENSE', which is part of this source code package.
#
# TODO: Make these dictionaries 'infinite'
NUMERIC = {'1': False, '2': False, '3': False, '4': False, '5': False, '6': False,
           '7': False, '8': False, '9': False}
ALPHABETIC = {'A': False, 'B': False, 'C': False, 'D': False, 'E': False, 'F': False, 'G': False,
              'H': False, 'I': False, 'J': False, 'K': False, 'L': False, 'M': False, 'N': False,
              'O': False, 'P': False, 'Q': False, 'R': False, 'S': False, 'T': False, 'U': False,
              'V': False, 'X': False, 'Y': False, 'Z': False}


class Style:
    def __init__(self, header=None, key_type='numeric', custom_keys=None, key_sep=': ', menu_size=None, col_spacing=5, col_sep='|'):
        if menu_size is None:
            self.menu_size = [5, 1]
        else:
            self.menu_size = menu_size

        self.header = header
        self.key_sep = key_sep
        self.col_spacing = ' ' * int((col_spacing - len(col_sep))/2)
        self.col_sep = col_sep

        if key_type == 'alphabetic_upper':
            self.keys = ALPHABETIC.copy()
        elif key_type == 'alphabetic_lower':
            self.keys = dict(zip(map(str.lower, ALPHABETIC.keys()), ALPHABETIC.values()))
        elif key_type == 'custom' and custom_keys is not None:
            self.keys = custom_keys
        else:
            self.keys = NUMERIC.copy()


DEFAULT = Style()
