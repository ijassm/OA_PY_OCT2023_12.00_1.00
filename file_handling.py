import os

# for i in range(1, 11):
#     f = open(f"myfile{i}.py", "x")
#     file = open(f"myfile{i}.py", "a")
#     file.write(f"print({i})")

for i in range(1, 11):
    os.remove(f"myfile{i}.py")


# demo = open("demo.txt", "wt")

# print(demo.write("it will overide existing text"))

# demo = open("demo.txt", "at")

# print(demo.write("it will append with existing text"))

# demo = open("demo.txt")

# print(demo.read())
# print(demo.readlines())
# print(demo.readline())
# print(demo.readline())
# print(demo.readline())
