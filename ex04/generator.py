import random


def generator(text, sep=" ", option=None):
    '''Option is an optional arg, sep is mandatory'''
    words = text.split(sep)
    if not isinstance(text, str):
        yield "ERROR"
        return
    if option:
        if not isinstance(option, str):
            yield "ERROR"
            return
        if option == 'shuffle':
            random.shuffle(words)
        elif option == 'unique':
            words = list(dict.fromkeys(words))
        elif option == 'ordered':
            words.sort()
        else:
            yield "ERROR"
            return
    for word in words:
        yield word
