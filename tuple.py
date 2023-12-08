t = (2, 3, 4, 5, 7)

# tuple is immutable

# t[0] = 5

print(type(t), "\n")

print(t[0])
print(t[1])
print(t[2])
print(t[3])
print(t[4], "\n")

print(t[-1])
print(t[-2])
print(t[-3])
print(t[-4])

# tuple is iterable

for i in t:
    print(i)
