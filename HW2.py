# prime numbers are greater than 1
def myPrime(x):
    if x > 1:
        for i in range(2, x):
            if (x % i) == 0:
                return False
    else:
        return False
    return True


def isPalindrome(x):
    y = str(x)
    return y == y[::-1]


def myFilter(L, func):
    newList = []
    for num in range(len(L)):
        if func(int(L[num])):
            newList.append(L[num])
    return newList


def myFilterMulti(L, funcL):
    newList = L
    for i in range(len(funcL)):
        newList = myFilter(newList, funcL[i])
    if not newList:
        return "Empty"
    return newList

def is_anagram(a,b):
    a = ''.join(sorted(a.lower()))
    b = ''.join(sorted(b.lower()))
    a = a.replace(" ", "")
    b = b.replace(" ", "")
    return a == b


L = [9,10,16,24,29,36,11]

print(myPrime(2))
print(isPalindrome(str(746)))
print(myFilter(L, myPrime))
print(myFilterMulti([1,9,10,16,24,55,131,149,181],[myPrime, isPalindrome]))
print(is_anagram("School master", "The classroom"))
print(is_anagram("Elior", "roli"))
print(is_anagram("Elior", " Liore "))


F = lambda x: x + 2
G = lambda x: (x**2 + 3*x - 2)
Y = lambda x,y: ((x+y)/(x-y)) if x != y else False

print(F(5),"\n",G(5),"\n",Y(5,6))

def integral(a,b,f):
    delta = (b - a)/100
    total = 0
    for i in range(100):
      total = total +  f(a + i * delta)*delta
    return total

def derivat(f):
    delta = 0.0001
    def g(x):
        return (f(x + delta) - f(x)) / delta
    return g

def like_fib(f):
    def g(n):
        return f(n-2) + f(n-1)
    return g

def smooth(f):
    g = lambda x:(f(x-1) + f(x) + f(x+1))/3
    return g

print(integral(0,1,lambda x:x**2))
print(derivat(lambda x:x**2)(3))
print(like_fib(lambda x:5-x)(3))
print(smooth(lambda x:5-x)(2))

def exp(x,n):
    result =1
    for n in range(n):
        result=result*x
    return result
def call_it(fn, n):
    return fn(n,3)
n=5
print(call_it(exp,n-3))