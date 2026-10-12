## Level 2 — Basic Logic Building (Questions 11–20)
# Focus: searching, counters, reversing, copying and comparing.

# 11. Search for a number in a list without using in.

# list = [1, 2, 3, 4, 5]
# target = 4
# found = False
# for num in list:
#     if num == target:
#         found = True
#         break
# if found == True:
#     print("number is in the list")
# else:
#      print("number is not in the list")

# 12. Count how many times a given number occurs in a list without using .count().

# list = [1, 2, 3, 4, 5, 4, 5, 4, 4]
# target = 1
# count = 0
# for num in list:
#     if num == target:
#         count = count + 1
# print(count)

# 13. Reverse a list without using .reverse() or slicing.

# original = [1, 2, 3, 4, 5]
# reverse = []
# for num in original:
#     reverse = [num] + reverse
# print(reverse)

# 14. Copy all elements from one list into another using a loop.

# original = [1, 2, 3, 4, 5]
# copied = []
# for num in original:
#     copied = copied + [num]
# print(original)
# print(copied)

# 15. Replace every negative number with zero in a list.

# list = [1, -5, 2, -4, -3]
# index = 0
# for i in list:
#     if i < 0:
#         list[index] = 0
#     index = index + 1
# print(list)
    
# 16. Create separate lists of even and odd numbers.

# numbers = [1, 2, 3, 4, 5]
# even_number = []
# odd_number = []
# for num in numbers:
#     if num % 2 == 0:
#         even_number = even_number + [num]
#     else:
#         odd_number = odd_number + [num]
# print(even_number)
# print(odd_number)

# 17. Check whether two lists are equal, including element order.

# number1 = [1, 2, 3]
# number2 = [1, 2, 3]
# print(number1 == number2)

# 18. Find all elements common to two lists.

# list1 = [1, 2, 3]
# list2 = [3, 4, 5]
# comman = []
# for item in list1:
#     if item in list2:
#         comman = comman + [item]
# print(comman)

# 19. Find elements present in the first list but not the second.

# list1 = [1, 2, 3]
# list2 = [3, 4, 5]
# result = []
# for item in list1:
#     if item in list2:
#         pass
#     else:
#         result = result + [item]
# print(result)

# 20. Check whether a tuple contains a given value without using in.

# my_tuple = (10, 20, 30, 40, 50)
# target_value = 30
# found = False
# for element in my_tuple:
#     if element == target_value:
#         found = True
#         break  
# print(found)


 