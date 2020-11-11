import math
import string

def XNOR(x, y):
    return (x == y)


print("XNOR test")
print(XNOR(True, False))
print(XNOR(True, True))
print(XNOR(False, False))
print(XNOR(False, True))


def RemoveMinDigit(x):                          #x is a number (Assumption is that x is a number)
    min = 9                                     #Min starts as the biggest number possible 9 so the comparrisons work correctly
    num = 0                                     #num contains the new number without the minimum digit
    for i in (str(x)):
        if int(i) < int(min) and int(i) != 0:
            min = i
        if min == 1:
            break
    print(min)
    for i in (str(x)):
        if i == str(min):
            continue
        num += int(i)
        num *= 10
    return num // 10


print("RemoveMinDigit Test:")
print(RemoveMinDigit(1234567))


def SquareArea(a, b, c, d, alpha, beta):
    s = (a + b + c + d) / 2             #a,b,c,d are the sides of the shape s is half of the perimeter
    return math.sqrt((s - a) * (s - b) * (s - c) * (s - d) - 0.5 * (a * b * c * d)* abs((1 + math.cos(math.radians(alpha + beta)))))

print("Test for SquareArea")
print("Enter a,b,c,d,alpha,beta in that exact order:")
print("", SquareArea(float(input()), float(input()), float(input()), float(input()), float(input()), float(input())))


def CheckArithmeticSeries(x):
    An = x % 10                 #An and An1 used to calculate the d which is the jump between every number
    An1 = x // 10               #Last anc current hold the current and previous value respectfully
    An1 = An1 % 10
    d = An - An1
    current = 0
    last = 0
    for i in (str(x)):
        last = current
        current = int(i)
        if (last == 0):
            continue
        if (current - last) == d:
            continue
        else:
            return False
    return True


print("CheckArithmeticSeries Test:")
print(CheckArithmeticSeries(2468))
print(CheckArithmeticSeries(14789))
print(CheckArithmeticSeries(1234567))


def CanBeTriangle(a, b, c):                                                     #a b and c are the sides of the triangle and are taken as floats
    if (a < 0 or b < 0 or c < 0 or a > (b + c) or b > (a + c) or c > (b + c)):
        return False
    return True


print("Test for Can be Triangle:")
print(CanBeTriangle(10.8, 57.4, 9.5), "\n", CanBeTriangle(3.333, 4.444, 5.555))


def CalcUpperCalcLower(x):
    countL = 0
    countU = 0
    for i in (str(x)):
        if i.islower():
            countL += 1
        if i.isupper():
            countU += 1
    print("Number of uppercase letters:", countU, "\n", "Number of lowercase letters", countL)


print("Test CalcUpperCalcLower:")
CalcUpperCalcLower("HeLlO im UPPER")


def PerfectNumber(x):  # Calculates if a number is a perfect number
    sum = 0  # By the sumation of all the numbers that divide x completly
    for i in range(1, int(x / 2) + 1):
        if (x % i) == 0:
            sum += i
    if sum == x:
        return True
    # print(sum)
    return False


print("Test PerfectNumber:")
print(PerfectNumber(8))


def IsPangrams(x):
    check = string.ascii_lowercase
    answer = [letter for letter in x.lower() if letter in check]
    return len(set(answer)) == len(check)


print("Test for IsPangrams:")
print(IsPangrams("The quick brown fox jumps over the lazy dog."))
print(IsPangrams("This is a wonderful day"))
