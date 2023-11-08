# matrix 5 * 5

# for i in range(5):
#     print("* " * 5)

# for i in range(1, 26):
#     print("*", end=" ")
#     if i % 5 == 0:
#         print()

# for i in range(2):
#     for j in range(2):
#         print(i, j)

# i = 0 has 2 loops
# j = 0 | j = 1

# output
# 0 0
# 0 1

# i = 1 has 2 loops
# j = 0 | j = 1

# output
# 1 0
# 1 1


# for i in range(2):
#     for j in range(2):
#         for k in range(2):
#             print(i, j, k)


"""
i = 0  => 2 j loops
    j = 0  => 2 k loops
        k = 0 | k = 1

output:
0 0 0
0 0 1
        
    j = 1  => 2 k loops
        k = 0 | k = 1
        
output:
0 1 0
0 1 1

-------i=0 ends-------

i = 1  => 2 j loops
    j = 0  => 2 k loops
        k = 0 | k = 1

output:
1 0 0
1 0 1
        
    j = 1  => 2 k loops
        k = 0 | k = 1
        
output:
1 1 0
1 1 1

-------i=1 ends-------
"""

for i in range(5):
    for j in range(5):
        print("*", end=" ")
    print()

"""
i = 0
    j = 0 | j = 1 | j = 2 | j = 3 | j = 4
line break
i = 1
    j = 0 | j = 1 | j = 2 | j = 3 | j = 4
line break
i = 2
    j = 0 | j = 1 | j = 2 | j = 3 | j = 4
line break
i = 3
    j = 0 | j = 1 | j = 2 | j = 3 | j = 4
line break
i = 4
    j = 0 | j = 1 | j = 2 | j = 3 | j = 4
"""
