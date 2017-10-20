""""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
# we know these identities:
#   a + b + c = 1000
#   a^2 + b^2 = c^2
#   a < b < c
# when combined and reduced, are:
#   1000a + 1000b - ab = 500,000
#   where a < b
# we know that there is only one combination of a and b that satisfy these conditions
# so we can break once we find the first solutions

a = 0
b = 0
c = 0

for i in range(2, 1000):
    for n in range(2, 1000):
        if (1000 * i) + (1000 * n) - (i * n) == 500000 and i < n:
            a = i
            b = n
            c = 1000 - i - n
            break

print('a = ' + str(a))
print('b = ' + str(b))
print('c = ' + str(c))
print('product = ' + str(a * b * c))
