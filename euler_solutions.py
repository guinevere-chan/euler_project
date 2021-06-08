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

# Problem 6
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum
# The sum of squares of the first 100 natural numbers
sum_of_squares = sum([n**2 for n in range(1, 101)])
# The square of sum of the first 100 natural numbers
square_of_sum = sum([n for n in range(1, 101)])**2

diff = square_of_sum - sum_of_squares
print(f"The difference between the sum of the squares of the first one hundred natural numbers and the square of the "
      f"sum is {diff}")

# Problem 7
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10001st prime number?
prime_number_list = [2, 3, 5, 7, 11]
i = 13
while len(prime_number_list) < 10001:
    if all([i % n != 0 for n in prime_number_list]):
        prime_number_list.append(i)
    i += 1
print(f"The 10001st prime number is {prime_number_list[-1]}")

# Problem 8
# The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832.
# Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of
# this product?

digit = 7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450

product_list = []
for i in range(len(str(digit))+1):
    thirteen_digit_set = str(digit)[i:i+13]
    product = np.product([int(d) for d in thirteen_digit_set])
    product_list.append(product)

print(f"The value of the greatest product is {max(product_list)}")


# Problem 9
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

# First find the abc options that sum to be 1000
for a in range(1, 400):
    for b in range(1, 400):
        c = (1000 - a) - b
        if a < b < c:
            if a ** 2 + b ** 2 == c ** 2:
                print(a * b * c)
