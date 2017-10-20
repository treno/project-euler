"""
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""
palindrome = 0
palindrome_i = 0
palindrome_n = 0

# start by considering the largest 3-digit number, 999
# repeat below process for all 3-digit numbers (i.e. until 100)
for i in range(999, 99, -1):
    # iteratively multiply number by progressively-smaller 3-digit numbers (i.e. 999, 998, ..., 100)
    for n in range(999, 99, -1):
        # only check factors once - without this condition, we would be duplicating checks
        if i <= n:
            product = str(i * n)
            produced_reversed = product[::-1]
            # check whether each product is a palindrome by casting it as a string and comparing it to its reverse
            # if palindrome and if larger than most recent palindrome found - replace stored value
            if product == produced_reversed and int(product) > palindrome:
                palindrome = int(product)
                palindrome_i = i
                palindrome_n = n

print('palindrome = ' + str(palindrome))
print('palindrome_i = ' + str(palindrome_i))
print('palindrome_n = ' + str(palindrome_n))
