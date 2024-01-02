def add(data):
    s = 0
    for i in data:
        s += i
    return s


def mul(data):
    s = 1
    for i in data:
        if i != 0:
            s *= i
    return s
