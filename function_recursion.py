def recursion(a):
    if a != 0:
        recursion(a - 1)
    print(a)


recursion(100)
