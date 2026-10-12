## Level 4 — Interview-Oriented Challenges (Questions 31–40)
# Focus: combining multiple ideas and thinking about edge cases.

# 31. Find the missing number from a list containing distinct numbers from 1 to n, with one number missing.

# num = [1, 2, 4, 5, 6]
# n = 6
# number = n * (n + 1) // 2
# total = 0
# for i in num:
#     total += i
# missing = number - total
# print(missing)

# 32. Find all duplicate values in a list without printing the same duplicate more than once.

# numbers = [1, 2, 3, 2, 3, 3]
# unique = []
# for num in numbers:
#     exist = False
#     for item in unique:
#         if item == num:
#             exist = True
#     if not exist:
#         unique = unique + [num]
# print(unique)

# 33. Find the intersection of two lists without duplicates.

# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# comman = []
# for x in list1:
#     for y in list2:
#         if x == y:
#             comman += [x]
# print(comman)

# 34. Split a list into two halves. Handle odd-length lists by placing the extra element in the second half.

# num = [1, 2, 3, 4, 5, 6]
# count = 0
# for i in num:  
#     count += 1
# half = count // 2
# first = []
# second = []
# i = 0
# for x in num:
#     if i < half:
#         first += [x]
#     else:
#         second += [x]
#     i += 1
# print(first)
# print(second)

# 35. Find the maximum difference later_element - earlier_element in a list, where the later element must come after the earlier element.

# 36. Find the longest consecutive run of equal elements.

# num = [1, 1, 2, 2, 2, 3, 3, 3, 0]
# current = 0
# longest = 0
# previous = []
# for i in num:
#     if i == previous:
#         current += 1
#     else:
#         current = 1
#     if current > longest:
#         longest = current
#     previous = i
# print(longest)

# 37. Check whether a list is sorted in nondecreasing order without using sort().

# num = [1, 2, 3, 4, 7]
# is_sorted = True
# previous = num[0]
# for i in num:
#     if i < previous:
#         is_sorted = False
#     previous = i
# print(is_sorted)

# 38. Flatten a list containing one level of nested lists.

# num = [
#     [1, 2],
#     [3, 4],
#     [5, 6]
# ]
# flat = []
# for x in num:
#     for y in x:
#         flat += [y]
# print(flat)

# 39. Given a tuple of (name, marks) pairs, find the student with the highest marks.

# students = (
#     ("bob", 78),
#     ("john", 92),
#     ("riya", 85)
# )
# namee = ""
# markss = 0
# for name, marks in students:
#     if marks > markss:
#         namee = name
#         markss = marks
# print(namee, markss)

# 40. Find all unique triplets whose sum equals a target.




