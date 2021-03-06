from itertools import product
from itertools import repeat

stop_list = ('is', 'it', 'are', 'our', 'my', 'the', 'they', 'and')

stem_rules = ('less', 'ship', 'ing', 'es', 'ly', 's')


def getBigrams(text):
    # map(bi_grams_calculating,map(stemming,map(numbers_removal,map(stopWords_removal,map(tokenization,text)))))
    text = tokenization(text)
    # print(text)
    text = stopWords_removal(text)
    # print(text)
    text = numbers_removal(text)
    # print(text)
    listToStr = ' '.join(map(str, text))
    text = listToStr.split()
    text = stemming(text)
    text = text.split()
    # print(text)
    # print(list(text))
    text = bi_grams_calculating(text)
    return text


def tokenization(text):
    new_str = ''
    text = text.split()
    for i in text:
        new_str += i.lower() + ' '
    return new_str.split()

    # text = map(lambda x: x.lower(), text.split())
    return text


def equal(x):
    for i in stop_list:
        if x == i:
            return True
    return False


def stopWords_removal(text):
    new_set = ''
    for i in text:
        if not equal(i):
            new_set += i + ' '

    return new_set.split()


def numbers_removal(text):
    text = filter(lambda x: not x.isnumeric(), text)
    return list(text)


def stemming(text):
    new_set = ''
    current, last = 0, 0
    for x in text:
        for i in stem_rules:
            if i in x:
                new_set += x.replace(i, '') + ' '
                current += 1
                break
        if current == last:
            new_set += x + ' '
        last = current

    return new_set


def bi_grams_calculating(text):
    return list(zip(text, text[1:]))


# def add(object_a,object_b):
# return object_a.perimeter + object_b.perimeter

class Triangle():
    def __init__(self, a, b, c):
        self.side_a = a
        self.side_b = b
        self.side_c = c
        # self.perimeter = a + b + c

    def __add__(self, other):
        return self.perimeter() + other.perimeter()

    def __repr__(self):
        return repr(
            'Triangle with sides equal ' + str(self.side_a) + ', ' + str(self.side_b) + ', and ' + str(self.side_c))

    def perimeter(self):
        return int(self.side_a + self.side_b + self.side_c)


class Square():
    def __init__(self, a):
        self.side = a

    def __add__(self, other):
        return self.perimeter() + other.perimeter()

    def perimeter(self):
        return int(self.side * 4)


def add(s, t):
    return s.perimeter() + t.perimeter()


class Node:
    def __init__(self, value):
        self.value = value
        self.point = None

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        res = ''
        ptr = self.head
        while ptr:
            res += str(ptr.value) + ", "
            ptr = ptr.point
        res = res.strip(", ")

        if len(res):
            return "[" + res + "]"
        else:
            return "[]"

    def __len__(self):
        i = 0
        head = self.head
        while head.point:
            head = head.point
            i += 1
        return i

    def insert(self, value):
        head = self.head
        tempNode = Node(value)

        if head is None:
            self.head = tempNode
            del tempNode
            return head
        while head.point:
            head = head.point
        head.point = tempNode
        del tempNode

    def insert_i(self, i, value):
        head = self.head
        helpNode = None
        tempNode = Node(value)
        for i in range(len(self)):
            helpNode = head
            head = head.point
        tempNode.point = head
        helpNode.point = tempNode

    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            point = current.point
            current.point = prev
            prev = current
            current = point
        self.head = prev

    def Remove(self, key):
        temp = self.head
        if temp is not None:
            if temp.value == key:
                self.head = temp.point
                temp = None
                return
        while temp is not None:
            if temp.value == key:
                break
            prev = temp
            temp = temp.point

        if temp == None:
            return
        prev.point = temp.point
        temp = None

    def Remove_i(self, n):
        first = self.head
        second = self.head
        if n == 0:
            self.head = self.head.point
            return
        for i in range(n):
            second = first
            first = first.point
        if first.point is None:
            second.point = None
            return
        second.point = second.point.point

    def Search(self, i):
        index = self.head
        while index.point is not None:
            if index.value == i:
                return index
            index = index.point
        return 'No value exists'


text = 'My 100 friends are very friendly They are keeping our friendship '
# print(text.split.stem())
# print(getBigrams(text))
t = Triangle(1, 2, 3)
print(t.perimeter())
s = Square(2)
print(s.perimeter())
print(s + s)
print(t + s)
print(add(s, t))
z = eval(repr(t))
print('z is ' + z)
print(t)

List = LinkedList()
List.insert(1)
List.insert(5)
List.insert(3)
List.insert(8)
List.insert_i(2, 10)
print(List)
List.reverse()
print(List)
List.Remove(10)
List.Remove_i(1)
Copy = List.Search(5)
print(List)
print(Copy)
