"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13 we can see that the 6th prime is 13.
What is the 10,001st prime number?
"""
# arbitrary upper limit we'll use when searching for the desired prime
LIMIT = 1000000
# desired prime to find
GOAL = 10001
# we store numbers and their "primeness" in a dictionary using boolean values
flags = {}
# we store all prime numbers we find in a list
primes = []
# we store the LIMITth prime number as our result
result = 0

# generate a dictionary of numbers from 2 to our upper threshold
# mark each of these numbers as a potential prime number by flagging each as "True"
for i in range(2, LIMIT):
    flags[i] = True

# we loop over all possible prime numbers, testing each candidate number for primeness
# when we disconfirm a candidate's primeness, we will change its flag value to False
# we start with 2, since we know it's the first prime
candidate = 2
while candidate <= LIMIT:
    # when we find a prime number, we remove all multiples of it since they necessarily are not prime
    if flags[candidate]:
        candidate_squared = candidate * candidate
        while candidate_squared <= LIMIT:
            flags[candidate_squared] = False
            candidate_squared += candidate
    # we increment the candidate and repeat until we hit out upper threshold
    candidate += 1

# after we test all numbers in our desired range, we store any that have the "True" flag in our primes list
for number in flags:
    if flags[number]:
        primes.append(number)

print(str(len(primes)) + ' primes total - ' + str(primes))
print(str(GOAL) + ' prime = ' + str(primes[GOAL - 1]))
