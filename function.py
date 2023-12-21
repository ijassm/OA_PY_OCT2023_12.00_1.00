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

# l1 = []


# def createList(n):
#     for i in range(1, n + 1):
#         l1.append(i)


# createList(15)
# print(l1)
# l1.clear()
# print("end")

# createList(5)
# print(l1)
# l1.clear()
# print("end")

# createList(5)


# -------------------------------------------------------

# Number of Arguments
"""By default, a function must be called with
the correct number of arguments. Meaning that
if your function expects 2 arguments, you have to
call the function with 2 arguments, not more, and not less."""


# This function expects 2 arguments, and gets 2 arguments:


# def my_function(fname, lname):
#     print(fname + " " + lname)


# my_function("Emil", "Refsnes")

# Arbitrary Arguments, *args

# def my_function(*names):
#     print(names)
#     print("The youngest child is " + names[2])


# my_function("Emil", "Tobias", "Linus")


# Keyword Arguments


# def my_function(name1, name2, name3):
#     print("The youngest child is " + name3)


# my_function(name3="john", name1="bala", name2="xyz")


# Arbitrary Keyword Arguments, **kwargs


# def my_function(**person):
#     print(person)
#     print("His last name is " + person["lname"])


# my_function(fname="Tobias", lname="Refsnes")


# Default Parameter Value


def my_function(country="Norway"):
    print("I am from " + country)


my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")
