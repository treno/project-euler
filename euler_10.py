"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""
# define limit under which we want to sum all prime numbers
LIMIT = 2000000
# store numbers and their "primeness" in a dictionary using boolean values
flags = {}
# store all prime numbers we find in a list
primes = []

# generate a dictionary of numbers from 2 to LIMIT
# mark these as a potential prime numbers by flagging each as "True"
for i in range(2, LIMIT):
    flags[i] = True

# loop over all possible prime numbers, testing each candidate number for primeness
# when we disconfirm a candidate's primeness, we change its flag value to False
# start with 2, since we know it's the first prime
candidate = 2
while candidate < LIMIT:
    # when we find a prime number, we remove all multiples of it since they necessarily are not prime
    if flags[candidate]:
        candidate_squared = candidate * candidate
        while candidate_squared <= LIMIT:
            flags[candidate_squared] = False
            candidate_squared += candidate
    # we increment the candidate and repeat until we exceed LIMIT
    candidate += 1

# after we test all numbers in our desired range, we store any that have the "True" flag in our primes list
for number in flags:
    if flags[number]:
        primes.append(number)

# store the sum of all primes under LIMIT as our result
result = sum(primes)

print(result)
