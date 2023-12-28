try:
    print(5 / 0)
    # print(name)
except ZeroDivisionError:
    raise Exception("you can't divide by zero")
except NameError:
    print("you can't able to access variable without decalaration")
else:
    print("finnally excecuted without no error")
finally:
    print("finnally excecuted")
