# Print a rectangle pattern of 5 rows and 5 columns using stars.

# for i in range(5):
#     for j in range(5):
#         print("*", end = " ")
#     print()

# Print the pattern:
# *
# * *
# * * *
# * * * *
# * * * * *

# for i in range(1, 6):
#     for j in range(i):
#         print("*", end = " ")
#     print()

# Print the pattern:
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

# for i in range(1, 6):
#     for j in range(1, i + 1):
#         print(j, end = " ")
#     print()

# Print the pattern:
# A
# A B
# A B C
# A B C D

# for i in range(1, 5):
#     for j in range(i):
#         print(chr(65 + j), end = " ")
#     print()

# Print multiplication tables from 1 to 10.

# for i in range(1, 11):
    # print("*****", i, "*****")
    # for j in range(1, 11):
    #     print(i, "x", j, "=", i*j)
    # print()

# Print:
# 5 5 5 5 5
# 5 5 5 5 5
# 5 5 5 5 5
# 5 5 5 5 5

# for i in range(5):
#     for j in range(5):
#         print("5", end = " ")
#     print()

# Print the pattern:
# 10
# 10 20
# 10 20 30
# 10 20 30 40

# for i in range(1, 5):
#     for j in range(1, i + 1):
#         print(j * 10, end = " ")
#     print()

# Print the pattern:
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

# for i in range(1, 6):
#     for j in range(i):
#         print(i, end = " ")
#     print()

# 2. Print the following pattern:
# 6
# 6 5
# 6 5 4
# 6 5 4 3
# 6 5 4 3 2
# 6 5 4 3 2 1

# for i in range(6, 0, -1):
#     for j in range(6, i - 1, -1):
#         print(j, end = " ")
#     print()

# A B C D E
# A B C D E
# A B C D E
# A B C D E
# A B C D E

# for i in range(5):
#     for j in range(65, 70):
#         print(chr(j), end = " ")
#     print()

# A A A A A
# B B B B B
# C C C C C
# D D D D D
# E E E E E

# for i in range(5):
#     for j in range(65, 70):
#         print(chr(65 + i), end = " ")
#     print()

# 1 0 1 0 1
# 0 1 0 1 0
# 1 0 1 0 1
# 0 1 0 1 0
# 1 0 1 0 1

# for i in range(5):
#     for j in range(5):
#         if(i + j) %2 == 0:
#             print(0, end = " ")
#         else:
#             print(1, end = " ")
#     print()

# 1 2 3 4
# 5 6 7 8
# 9 10 11 12
# 13 14 15 16

# for i in range(1, 17, 4):
#     for j in range(4):
#         print(i + j, end = " ")
#     print()