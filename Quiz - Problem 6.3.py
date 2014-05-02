#def probTest(limit):
#    pass

def probTest(limit):
    i = 1
    prob = 1.0 / 6
    while prob > limit:
        prob = float((5 ** i)) / (6 ** (i + 1))
        i += 1
    return i