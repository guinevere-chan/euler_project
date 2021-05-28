import pandas as pd
import numpy as np
import itertools

# Problem 1
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000

num_list = []
for i in range(999):
    if (i + 1) % 3 == 0 or (i + 1) % 5 == 0:
        num_list.append(i + 1)

print(sum(num_list))

# Problem 2
# Each new term in the Fibonacci sequence is generated by adding the previous two terms.
# By starting with 1 and 2, the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed four million,
# find the sum of the even-valued terms.

fibonacci_list = []
for i in range(100000000):
    if i == 0:
        i = 1
    else:
        i = fibonacci_list[i - 1] + fibonacci_list[i - 2]
    fibonacci_list.append(i)
    if max(fibonacci_list) > 4000000:
        break

fibonacci_even_list = []
for num in fibonacci_list[:-1]:
    if num % 2 == 0:
        fibonacci_even_list.append(num)

print(sum(fibonacci_even_list))

# Problem 3
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
# The number should be a prime number.
# The number should divide the number perfectly.

num = 600851475143
prime_list = []
for i in range(2, num):
    if num % i == 0:
        prime_list.append(i)
    if np.product(prime_list) == 600851475143:
        break

print(max(prime_list))

# Problem 4
# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

combo = list(itertools.product([i for i in range(100, 999)], repeat=2))
multiply_combo = [x * y for x, y in combo if str(x * y) == str(x * y)[::-1]]

print(max(multiply_combo))

# Problem 5
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
i = 1
for i in range(20, 100000000000, step=20):
    if all([i % n == 0 for n in range(1, 20)]):
        print(f"The smallest positive number that is evenly divisible by all of the numbers from 1 to 20 is {i}")
        break
    i += 1
