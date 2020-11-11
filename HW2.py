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

print(myPrime(9))
print(isPalindrome(str(746)))
print(myFilter(L, myPrime))
print(myFilterMulti([1,9,10,16,24,55,131,149,181],[myPrime, isPalindrome]))
print(is_anagram("School master", "The classroom"))
print(is_anagram("Elior", "roli"))
print(is_anagram("Elior", " Liore "))