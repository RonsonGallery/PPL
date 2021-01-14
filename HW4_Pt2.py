from functools import reduce
from math import *
from operator import mul


class Exp(object):
    def __init__(self, operator, operands):
        self.operator = operator
        self.operands = operands

    def __repr__(self):
        return 'Exp({0}, {1})'.format(repr(self.operator), repr(self.operands))

    def __str__(self):
        operand_strs = ", ".join(map(str, self.operands))
        return "{0}({1})".format(self.operator, operand_strs)

    def calc_eval(exp):
        if type(exp) in (int, float):
            return exp
        elif type(exp) == Exp:
            arguments = list(map(exp.calc_eval, exp.operands))
        return calc_apply(exp.opeartor, arguments)


def calc_apply(operator, args):
    if operator in ("add", "+"):
        return sum(args)
    if operator in ("sub", "-"):
        if len(args) == 0:
            raise TypeError(operator + "requires at least 1 rgument")
        if len(args) == 1:
            return -args[0]
        return sum(args[:1] + [-arg for arg in args[1:]])

    if operator in ("mul", "*"):
        return reduce(mul, args, 1)

    if operator in ("div", "/"):
        if len(args) != 2:
            raise TypeError(operator + "requires exactly 2 arguments")
        numer, denom = args[0], args[1]
        return numer / denom

    if operator in ("pow", "^"):
        if len(args) != 2:
            raise TypeError(operator + "requires exactly 2 arguments")
        return args[0] ** args[1]

    if operator in ("modolo", "%"):
        if len(args) != 2:
            raise TypeError(operator + "requires exactly 2 arguments")
        return args[0] % args[1]


# print(sum(args[:1] + [-arg for arg in args[1:]]))
# print(args)
print(calc_apply('+', [1, 2, 3]))
print(calc_apply('^', [2, 2]))
print(calc_apply('%',[4, 2]))
print(calc_apply('/',[8,2]))
