"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13 we can see that the 6th prime is 13.
What is the 10,001st prime number?
"""
LIMIT = 100
list_of_primes = [2]

# since no prime numbers are even, we can loop over odds only (starting with 3 and step by 2)
for candidate_prime in range(3, LIMIT * LIMIT, 2):
    print('\n' + 'candidate = ' + str(candidate_prime))
    # check to see if we have the LIMITth prime number
    # if we don't, continue to generate prime numbers until we get it
    if len(list_of_primes) != LIMIT:
        for n in list_of_primes:
            print('n = ' + str(n))
            # if the candidate prime is already in our list
            # or if it evenly divides into a prime number less than it
            # we know it's not prime and we can break and try the next candidate
            if candidate_prime in list_of_primes or candidate_prime % n == 0:
                break
            # if we try to divide the candidate by all prime numbers smaller than itself
            # and every divisor generates a non-zero remainder, we know the
            # number is prime and we add it to our growing list of prime numbers
            elif list_of_primes.index(n) == len(list_of_primes) - 1:
                list_of_primes.append(candidate_prime)
                print(list_of_primes)
                print(len(list_of_primes))
    # if we do have the LIMITth prime number, break and print answer
    else:
        break

print(list_of_primes[LIMIT - 1])
