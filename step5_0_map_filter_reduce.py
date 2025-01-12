from functools import reduce
from operator import add

nums = [1, 2, 3, 4, 5]

# Using map to square each number
squared = list(map(lambda x: x * x, nums))  # [1, 4, 9, 16, 25]

# Using filter to keep only even numbers
evens = list(filter(lambda x: x % 2 == 0, nums))  # [2, 4]

# Using reduce to calculate the sum of all numbers
total = reduce(add, nums, 0)  # 15

print("Original numbers:", nums)
print("Squared numbers:", squared)
print("Even numbers:", evens)
print("Sum of numbers:", total)
print(list(map(lambda x, y: x + y, [1, 2], [3, 4])))