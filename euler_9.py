""""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
# define input parameter
LIMIT = 1000
a = 0
b = 0
c = 0

# we know these identities:
#   a + b + c = LIMIT
#   a^2 + b^2 = c^2
#   a < b < c
# when combined and reduced, these are:
#   (LIMIT * a) + (LIMIT * b) - ab = (LIMIT * LIMIT)/ 2
#   where a < b
# since we know that there is only one combination of a and b that satisfy these conditions
# we can break once we find the first solution

for i in range(2, LIMIT):
    for n in range(2, LIMIT):
        if (LIMIT * i) + (LIMIT * n) - (i * n) == (LIMIT * LIMIT) / 2 and i < n:
            a = i
            b = n
            c = LIMIT - i - n
            break

print('a = ' + str(a))
print('b = ' + str(b))
print('c = ' + str(c))
print('product = ' + str(a * b * c))
