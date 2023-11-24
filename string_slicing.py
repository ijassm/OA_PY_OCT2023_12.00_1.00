a = "hello world"


print(a)

# syntax
# a[start:stop:step]

print(a[0:7:1])
print(a[:7:1])
print(a[::1])
print(a[::])

print(a[6:11:])
print(a[6::])
print(a[6::1])

print(a[-5::1])
print(a[-5::])

print("malayalam"[-1::-1])
print("race"[::-1])

a = "race"[::-1]

for i in a:
    print(i)