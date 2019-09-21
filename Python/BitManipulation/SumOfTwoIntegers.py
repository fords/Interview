'''
Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Example 1:

Input: a = 1, b = 2
Output: 3
Example 2:

Input: a = -2, b = 3
Output: 1
'''

def getSum(a , b ):
    mask = 0xFFFFFFFF
    while b & mask != 0 :

        carry = a & b
        a = a ^ b
        b = carry << 1

    return a if b < mask else (a & mask)


'''
Explanation

a        1 0 1
b        0 1 0
res =    1 1 1   a ^ b

a      0 1 1
b      0 1 0
carry  0 1 0    << 1
actual carry 1 0 0 after 1 left shift

The carry becomes b again which would be added to a until carry becomse zero
'''
