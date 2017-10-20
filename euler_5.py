"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
n = 20
candidate = 1
remainder = 1

while remainder != 0:
    remainder = 0
    print('\ncandidate = ' + str(candidate))
    for i in range(n, 1, -1):
        print('i = ' + str(i))
        remainder += candidate % i
        print('r = ' + str(remainder))
        # jump to next candidate as soon as remainder > 0
        if remainder != 0:
            break
    # all viable candidates must be divisible by primes <= n
    # e.g. if n = 20, n must be divisible by 2x3x5x7x11x13x17x19 = 9699690
    if candidate == 1:
        candidate += 9699689
    elif remainder != 0:
        candidate += 9699690

print('\n' + str(candidate))
