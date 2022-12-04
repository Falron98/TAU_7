from assertpy import add_extension


def is_legal_value(self):
    if self.val < 0 or self.val % 5 != 0:
        return self.error(f'{self.val} is illegal value!')
    return self


def not_int(self):
    if self.val is not int:
        return self.error(f'{self.val} is not int')


add_extension(is_legal_value())
add_extension(not_int())
