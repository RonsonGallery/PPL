from itertools import product
from itertools import repeat

stop_list =  ('is', 'it', 'are', 'our', 'my', 'the', 'they', 'and')

stem_rules = ('less', 'ship', 'ing', 'es', 'ly', 's')


def is_in_stop_list(word):
    if word in stop_list and not word.numberic:
        return False
    return True


def text_preprocessing(text, stopwords):
    bag_words = {}
    filterd = filter(lambda x: x not in stopwords and not x.isnumeric(), map(lambda x: x.lower(), text.split()))
    for i in filterd:
        if i in bag_words:
            bag_words[i] += 1
        else:
            bag_words[i] = 1
    return bag_words


# print(text_preprocessing('My cat is 10 and it is a very fat cat',stop_list))


def getBigrams(text):
    #map(bi_grams_calculating,map(stemming,map(numbers_removal,map(stopWords_removal,map(tokenization,text)))))
    text = tokenization(text)
    print(text)
    text = stopWords_removal(text)
    print(text)
    text = numbers_removal(text)
    print(text)
    listToStr = ' '.join(map(str, text))
    #str1.join(text)
    #text = str1
    text = listToStr.split()
    text = stemming(text)
    text = text.split()
    print(text)
    print(list(text))
    text = bi_grams_calculating(list(text))
    return text

def tokenization(text):
    new_str = ''
    text = text.split()
    for i in text:
        new_str += i.lower() + ' '
    return new_str.split()

    #text = map(lambda x: x.lower(), text.split())
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

        # += i + ' '
    #text = filter(lambda x: x not in stop_list, text)
    return new_set.split()

def numbers_removal(text):
    text = filter(lambda x: not x.isnumeric(), text)
    return list(text)

def stemming(text):
    new_set = ''
    current,last = 0,0
    for x in text:
        for i in stem_rules:
            if i in x:
                new_set += x.replace(i,'') + ' '
                current += 1
                break
        if current == last:
            new_set += x + ' '
        last = current

    return new_set


def bi_grams_calculating(text):
    return list(zip(text,text[1:]))
    """
    new_str = ''
    current = text[0]
    for i in text:
        if i != current:
            #place_holder = (current,i)
            new_str += '(' + current + ','+ i  +      ')' ','

        current = i
    return '(' + new_str[:-1] + ')'
    """

"""
    def dispatch(msg):
        if msg == 'tokenization':
            return tokenization
        if msg == 'numbers_removal':
            return numbers_removal
        elif msg == 'stopWords_removal':
            return stopWords_removal
        elif msg == 'stemming':
            return stemming()
        elif msg == 'bi_grams_calculating':
            return bi_grams_calculating()
        return dispatch
"""

text = 'My 100 friends are very friendly They are keeping our friendship '
#print(text.split.stem())
print(getBigrams(text))