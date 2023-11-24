# even1 = 2
# even2 = 4
# even3 = 6
# odd1 = 1
# odd2 = 3
# odd3 = 5



even = [2,4]
odd = [1,3]

print(even)
print(odd)
print(type(even), type(odd))

print(even[0])
print(even[1])


print(even, "before")
# mutable
even[0] = 6
even.append(8)
print(even, "after")

