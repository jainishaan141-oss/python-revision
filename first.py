# 1. What is time complexity?

# describe how number of operations performed by an algorithm grows as input size increases;.

# 2. What does n represent?

# we commonly use n to represent the size of the input.

# 3. What is Big O notation?

# the growth rate of an algorithm as input size increases.

# 4. Why is accessing a list element by index O(1)?

# it's called constant time
# very efficient
# the number of operations does not depend on the input size.

# 5. Why are two nested loops often O(n²)?

# commonly occurs when one loop runs inside another loop, and both loops depend on n.

# 6. Write a program to count how many digits are present in a positive integer without converting it into a string.
# Expected output:
# Task: Identify the time complexity with respect to the number of digits.

# def count_digits(n):
#     if n == 0:
#         return 1
#     count = 0
#     while n > 0:
#         n = n // 10  
#         count += 1   
#     return count
# number = 12345
# print(f"Number of digits in {number} is: {count_digits(number)}")

# it has 5 opeartions, and solve with a O(n)

# 7. Question 5. Print a number pattern
# Write a program to print the following pattern for n = 4:
# Expected output:
# Task: Identify the time complexity.

# n = 4
# for i in range(n):          
#     for j in range(n):      
#         print(j + 1, end=" ")
#     print()

# it has 16 operations, and solve with a O(n^2)


