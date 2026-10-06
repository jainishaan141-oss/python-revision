# Level 1 — Understand the for Loop

# 1. Print numbers from 1 to 10
# Expected:
# 1
# 2
# 3
# 10
# **Skill:** Basic `for` loop and `range()`.

# for i in range(1, 11):
#     print(i)

### 2. Print numbers from 10 to 1
# Expected:
# 10
# 9
# 8
# 1
# **Skill:** Understanding `range(start, stop, step)`.

# for i in range(10, 0, -1):
#     print(i)

# 3. Print all even numbers from 1 to 20
# Expected:
# 2 4 6 8 10 12 14 16 18 20
# **Skill:** `for` + `if` + `%`.

# for i in range(1, 21):
    # if i %2 == 0:
        # print(i)

# 4. Print all odd numbers from 1 to 20
# Expected:
# 1 3 5 7 9 11 13 15 17 19

# for i in range(1, 20, 2):
#     print(i)

# 5. Print the first 10 multiples of 5
# Expected:
# 5 10 15 20 25 30 35 40 45 50
# **Skill:** Generating values rather than simply printing a range.

# for i in range(1, 11):
#     print(i * 5)

# Level 2 — Counting and Summation
# These are extremely important for logic building.

# 6. Find the sum of numbers from 1 to 100
# Expected:
# 5050
# Student should discover the idea:
# total = 0
# then repeatedly add.

# total = 0
# for i in range(1, 101):
#     total = total + i
# print(total)

# 7. Find the sum of all even numbers from 1 to 100
# Expected:
# 2550

# total = 0
# for i in range(1, 101):
#     if i %2 == 0:
#         total = total + i
# print(total)

# 8. Find the sum of all odd numbers from 1 to 100
# Expected:
# 2500

# total = 0
# for i in range(1, 100, 2):
#     total = total + i
# print(total)

# 9. Count how many numbers between 1 and 100 are divisible by 7
# Expected:
# 14
# Important thinking:
# What should I count?
# When should I increase the counter?

# count = 0
# for i in range(1, 101):
#     if i %7 == 0:
#         count = count + 1
# print(count)

# 10. Count numbers between 1 and 100 that are divisible by both 3 and 5
# Expected:
# 6
# This introduces:
# if number % 3 == 0 and number % 5 == 0:

# count = 0
# for i in range(1, 101):
#     if i %3 == 0 and i %5 == 0:
#         count = count + 1
# print(count)
 
