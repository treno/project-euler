"""
The sum of the squares of the first ten natural numbers is, 12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is, (1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers
and the square of the sum is 3025 − 385 = 2640.
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""
NUMBERS = 100
sum_of_squares = 0
sum_of_numbers = 0

# calculate the sum of the squares and the sum of each number in range
# we then square the sum of this second number and subtract the first number from it
# to get our answer
for i in range(NUMBERS + 1):
    sum_of_squares += i * i
    sum_of_numbers += i

square_of_sum = sum_of_numbers * sum_of_numbers
result = square_of_sum - sum_of_squares

print(result)
