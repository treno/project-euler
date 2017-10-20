"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143?
"""
# the input number is the largest possible candidate for largest prime factor
# (is the case if the input number is prime)
n = 600851475143
divisor = 2

while divisor < n:
    # start by checking if the input number divides evenly by 2
    while n % divisor == 0 and n != divisor:
        # if so, we know the input number isn't prime
        # and we replace n's value with the new candidate for largest prime factor (i.e. n / divisor)
        n = n / divisor
    # repeat this, iteratively testing bigger divisors to determine if any divide evenly into the current candidate
    divisor += 1
    # repeat this until no numbers divide evenly into the candidate except for the candidate itself
    # we are left with the largest prime factor

print(int(n))
