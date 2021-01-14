class Euro():
    def __init__(self, amount):
        self.amount = amount

    def __str__(self):
        return str(self.amount)

    def __repr__(self):
        return repr('Euro ' + self.amount)


class Dollar():
    def __init__(self, amount):
        self.amount = amount

    def __str__(self):
        return str(self.amount)

    def __repr__(self):
        return repr('Dollar ' + self.amount)


class Sekel():
    def __init__(self, amount):
        self.amount = amount

    def __str__(self):
        return str(self.amount)

    def __repr__(self):
        return repr('Dollar ' + self.amount)

#for ease of use will convert differnt types to sekel

def convert(arg):
    if (type(arg) == Sekel):
        return arg
    if type(arg) == Euro:
        return arg.amount * 3.7
    if type(arg) == Dollar:
        return arg.amount * 3.2


def apply(operand, arg1, arg2):
    if operand == 'add':
        if type(arg1) == type(arg2):
            return arg1.amount + arg2.amount
        if type(arg1) != type(arg2):
            return convert(arg1) + convert(arg2)
    if operand == 'mul':
        if type(arg1) == type(arg2):
            return arg1.amount * arg2.amount
        if type(arg1) != type(arg2):
            return convert(arg1) * convert(arg2)


currency = Euro(5)
currency2 = Dollar(3)
currency3 = Euro(2)
currency4 = Dollar(8)
print(apply('add', currency, currency2))
print(apply('mul', currency, currency2))
print(apply('add', currency, currency3))
print(apply('add', currency2, currency4))
