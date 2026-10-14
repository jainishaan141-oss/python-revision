# Level 3 — Dictionary Logic Building

# 11. Character frequency counter
# Count how many times each character occurs in a string without using `Counter`.
# Example: `"banana"` → `{"b": 1, "a": 3, "n": 2}`.

# text = "banana"
# result = {}
# for ch in text:
#     if ch in result:
#         result[ch] += 1
#     else:
#         result[ch] = 1
# print(result)

# 12. Word frequency counter
# Count the occurrences of every word in a sentence. Treat uppercase and lowercase versions as the same word.
# Example: `"Python is easy and python is useful"`.

# text = "Python is easy and python is useful"
# result = {}
# current_word = ""
# for char in text:
#     if char == " ":
#         if current_word != "":
#             if current_word in result:
#                 result[current_word] += 1
#             else:
#                 result[current_word] = 1
#             current_word = ""  
#     else:
#         current_word += char
# if current_word != "":
#     if current_word in result:
#         result[current_word] += 1
#     else:
#         result[current_word] = 1
# print(result)

# 13. Find the most frequent element
# Given a list of numbers, use a dictionary to find the number that appears most often.

# numbers = [1, 2, 3, 2, 3, 3]
# count = {}
# for num in numbers:
#     if num in count:
#         count[num] += 1
#     else:
#         count[num] = 1
# comman = 0
# maximum = 0
# for num in count:
#     if count[num] > maximum:
#         maximum = count[num]
#         comman = num
# print(comman)

# 14. Group words by their first letter
# Given ["apple", "ant", "ball", "bat", "cat"], create a dictionary grouping words by their first letter.

# words = {"apple", "ant", "ball", "bat", "cat"}
# result = {}
# for word in words:
#     first = word[0]
#     if first in result:
#         result[first] += [word]
#     else:
#         result[first] = [word]
# print(result)

# 15. Inventory management
# Create a product inventory dictionary. Allow the program to update stock after a sale, reject a sale when stock is insufficient, and display the remaining stock.

# Uniqueness, membership, intersections, comparisons and combinations
## Level 1 — Set Fundamentals

# 16. Remove duplicates from a list
# Convert [1, 2, 2, 3, 4, 4, 5] into a set and display the unique values.

# numbers = [1, 2, 3, 2, 3, 3]
# unique = {numbers[0]}
# for num in numbers:
#     unique = unique | {num}
# print(unique)

# 17. Count unique values
# Find the number of distinct elements in a list using a set.

# numbers = [1, 2, 2, 3, 4, 4, 5]
# unique = {numbers[0]}
# count = 1
# for num in numbers:
#     if num not in unique:
#         unique = unique | {num}
#         count += 1
# print(count)

# 18. Find common elements
# Given two lists, use sets to find the elements common to both.

# list1 = [1, 2, 3, 4, 5]
# list2 = [4, 5, 6, 7, 8]
# common = []
# for num in list1:
#     if num in list2:
#         common = common + [num]
# print(common)

# 19. Find elements present in only one set
# Given two sets, find elements that belong to the first set but not the second.

# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}
# first = []
# for x in set1:
#     found = False
#     for y in set2:
#         if x == y:
#             found = True
#     if found == False:
#         first += [x]
# print(first)

# 20. Find the symmetric difference
# Given two sets, return the elements that belong to either set, but not both.

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
result = []
for a in set1:
    found = False
    for b in set2:
        if a == b:
            found = True
    if found == False:
        result = result + [a]
for b in set2:
    found = False
    for a in set1:
        if a == b:
            found = True
    if found == False:
        result = result + [b]
print(result)





