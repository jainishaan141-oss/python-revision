# Level 2 — Set Problem-Solving

# 21. Check whether two lists contain the same unique values
# Check whether two lists have the same set of distinct elements, even if their order and duplicate counts differ.

# list1 = [1, 2, 3, 2, 1]
# list2 = [3, 2, 1, 1, 3]
# same = True
# for a in list1:
#     found = False
#     for b in list2:
#         if a == b:
#             found = True
#     if found == False:
#         same = False
# for b in list2:
#     found = False
#     for a in list1:
#         if b == a:
#             found = True
#     if found == False:
#         same = False
# if same:
#     print("same values")
# else:
#     print("different values")

# 22. Find missing values
# Given the set of expected IDs {1, 2, 3, 4, 5, 6} and received IDs {1, 3, 4, 6}, find the missing IDs.

# expected = {1, 2, 3, 4, 5, 6}
# received = {1, 3, 4, 6}
# for a in expected:
#     found = False
#     for b in received:
#         if a == b:
#             found = True
#     if found == False:
#         print(a)

# 23. Find duplicate values using a set
# Identify all values that appear more than once in a list. Return each duplicate only once.

# numbers = [1, 2, 3, 2, 4, 1, 5, 2]
# duplicates = []
# for a in numbers:
#     count = 0
#     for b in numbers:
#         if a == b:
#             count += 1
#     if count > 1:
#         already = False
#         for c in duplicates:
#             if c == a:
#                 already = True
#         if already == False:
#             duplicates += [a]
# print(duplicates)

# 24. Find common characters in two strings
# Given two strings, find their common distinct characters.

# string1 = "hello"
# string2 = "world"
# comman = ""
# for a in string1:
#     for b in string2:
#         if a == b:
#             already = False
#             for c in comman:
#                 if c == a:
#                     already = True
#             if already == False:
#                 comman += a
# print(comman)

# 25. Check whether two strings are anagrams using sets and dictionaries
# Determine whether two strings contain the same letters with the same frequencies. Ignore spaces and letter case. Explain why sets alone are insufficient.

# Level 3 — Interview-Oriented Set Challenges

# 26. Find students enrolled in both courses
# Given two sets of student IDs for two courses, find the students enrolled in both.

# course1 = [101, 102, 103, 104, 105]
# course2 = [103, 105, 108, 109, 101]
# for i in course1:
#     for j in course2:
#         if i == j:
#             print(i)

# 27. Find students enrolled in exactly one course
# Given two sets of student IDs, find students enrolled in one course but not both.

# course1 = [101, 102, 103, 104, 105]
# course2 = [103, 105, 108, 109, 101]
# for a in course1:
#     found = False
#     for b in course2:
#         if a == b:
#             found = True
#     if found == False:
#         print(a)
# for b in course2:
#     found = False
#     for a in course1:
#         if b == a:
#             found = True
#     if found == False:
#         print(b)

# 28. Check whether one set is a subset of another
# Determine whether all required skills in one set are contained in another set.

# str1 = ["python", "java"]
# str2 = ["python", "sql", "java"]
# subset = True
# for a in str1:
#     found = False
#     for b in str2:
#         if a == b:
#             found = True
#     if found == False:
#         subset = False
# if subset:
#     print("subset")
# else:
#     print("not subset")

# 29. Find the first repeated element
# Given a list, use a set to find the first value that appears for a second time.

numbers = [5, 3, 8, 3, 5, 9]
repeated= []
for i in numbers:
    already = False
    for j in repeated:
        if j == i:
            already = True
    if already:
        print(i)
        break
    repeated += [i]


