# 1. Print a 6 × 6 hollow square using.

# size = 6
# for i in range(size):
#     for j in range(size):
#         if i == 0 or i == size - 1 or j == 0 or j == size - 1:
#             print(".", end = " ")
#         else:
#             print(" ", end = " ")
#     print()

# 2. Print the following pattern:
# 6
# 6 5
# 6 5 4
# 6 5 4 3
# 6 5 4 3 2
# 6 5 4 3 2 1

# for i in range(6, 0, -1):
#     for j in range(6, i -1, -1):
#         print(j, end = " ")
#     print()

# 3.
# A B C D E
# A B C D E
# A B C D E
# A B C D E
# A B C D E

# for i in range(5):
#     for j in range(65, 70):
#         print(chr(j), end = " ")
#     print()

# 4.
# A A A A A
# B B B B B
# C C C C C
# D D D D D
# E E E E E

# for i in range(65, 70):
#     for j in range(5):
#         print(chr(i), end = " ")
#     print()

# 5.
# 1 0 1 0 1
# 0 1 0 1 0
# 1 0 1 0 1
# 0 1 0 1 0
# 1 0 1 0 1

# for i in range(5):
#     for j in range(5):
#         if (i + j) % 2 == 0:
#             print(1, end = " ")
#         else:
#             print(0, end = " ")
#     print()

# 6. 
# 1 2 3 4
# 5 6 7 8
# 9 10 11 12
# 13 14 15 16

# for i in range(1, 17, 4):
#     for j in range(4):
#         print(i + j, end = " ")
#     print()



