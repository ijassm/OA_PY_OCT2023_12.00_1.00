# A function is a block of code which only runs when it is called.

# You can pass data, known as parameters, into a function.

# A function can return data as a result.

# Creating a Function

# In Python a function is defined using the def keyword:


# def greeting(name):
#     print("hello " + name)


# print("start")

# greeting("bala")

# print("end")

# greeting("ajay")

l1 = []


def createList(n):
    for i in range(1, n + 1):
        l1.append(i)


createList(15)
print(l1)
l1.clear()
print("end")

createList(5)
print(l1)
l1.clear()
print("end")

# createList(5)
