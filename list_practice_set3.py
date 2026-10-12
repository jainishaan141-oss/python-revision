# Level 3 — Intermediate Problem Solving (Questions 21–30)
# Focus: nested loops, tracking values, handling duplicates and transforming data.

# 21. Find the second-largest distinct element without using sort() or max().

# numbers = [1, 2, 3, 4, 5, 6, 7]
# largest = float('-inf')
# second_largest = float('-inf')
# for num in numbers:
#     if num > largest:
#         second_largest = largest
#         largest = num
#     elif num > second_largest and num != largest:
#         second_largest = num
# print(largest)
# print(second_largest)

# 22. Find the second-smallest distinct element without using sort() or min().

# numbers = [1, 2, 3, 4, 5, 6, 7]
# smallest = float('inf')
# second_smallest = float('inf')
# for num in numbers:
#     if num < smallest:
#         second_smallest = smallest
#         smallest = num
#     elif num < second_smallest and num != smallest:
#         second_smallest = num
# print(smallest)
# print(second_smallest)

# 23. Remove duplicate elements while preserving their original order.

# list = [1, 1, 2, 3, 4, 5, 5]
# unique = []
# for num in list:
#     exist = False
#     for item in unique:
#         if item == num:
#             exist = True
#     if not exist:
#         unique = unique + [num]
# print(unique)

# 24. Find the frequency of every distinct element in a list.

# list = [1, 2, 3, 2, 3, 3]
# frequency = {}
# for num in list:
#     if num in frequency:
#         frequency[num] += 1
#     else:
#         frequency[num] = 1
# print(frequency)

# 25. Move all zeros to the end while preserving the order of nonzero elements.

# list = [1, 0, 2, 0, 3, 0]
# list1 = []
# count = 0
# for i in list:
#     if i != 0:
#         list1 += [i]
#     else:
#         count += 1
# list1 += [0] * count
# print(list1)

# 26. Rotate a list one position to the right.

# 27. Merge two lists and produce a sorted result without using .sort() or sorted().

# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# merged = list1 + list2
# count = 0
# for element in merged:
#     count += 1
# for i in range(count):
#      for j in range(count - 1):
#         if merged[j] > merged[j + 1]:
#             temp = merged[j]
#             merged[j] = merged[j + 1]
#             merged[j + 1] = temp
# print(merged)

# 28. Find all pairs of elements whose sum equals a target.

# numbers = [2, 4, 3, 5, 7, 8, 9]
# target = 10
# length = 0
# for item in numbers:
#     length += 1
# for i in range(length):
#     for j in range(i + 1, length):
#         if numbers[i] + numbers[j] == target:
#             print(numbers[i], numbers[j])

# 29. Check whether a tuple is a palindrome.

# tuple = (1, 2, 3, 2, 1)
# reverse = ()
# for item in tuple:
#     reverse = (item,) + reverse
# if tuple == reverse:
#     print("palindrome")
# else:
#     print("not palindrome")

# 30. Find the element that appears most frequently in a list.

# list = [1, 3, 2, 3, 4, 3, 2, 3, 1]
# most_frequent = list[0]
# highest_count = 0
# for item in list:
#     counted = 0
#     for i in list:
#         if i == item:
#             counted += 1
#     if counted > highest_count:
#         highest_count = counted
#         most_frequent = item
# print(most_frequent)





