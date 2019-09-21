'''
Reverse bits of 32 bits unsigned integers
Input: 00000010100101000001111010011100
Output: 00111001011110000010100101000000
'''

def reverseBits(self, n):
    res = 0
    for i in range(32):
        res = (res<<1) + (n&1)
        n>>=1
        # print "{0:b}".format(n)
    return res
