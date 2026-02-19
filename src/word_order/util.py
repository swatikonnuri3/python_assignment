def find_word_order(n, words):
    dct = {}
    for w in words:
        if w in dct:
            dct[w] += 1
        else:
            dct[w] = 1
    return dct