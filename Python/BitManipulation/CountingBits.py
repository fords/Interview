'''
Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation
 and return them as an array.

Example 1:

Input: 2
Output: [0,1,1]
Example 2:

Input: 5
Output: [0,1,1,2,1,2]
Follow up:

It is very easy to come up with a solution with run time O(n*sizeof(integer)).
But can you do it in linear time O(n) /possibly in a single pass?
'''


# O(n) concise - slicing and shallow copy
def countingBits_concise(num):
    arr = [0]
    if num > 0:
        while len(arr) < num + 1:
            for x in arr[:]:
                arr.extend([x+1])
    return arr[0:num+1]


# optimized O(n) using dynamic programming
def countingBits(num):
    dp = [0] * (num + 1)
    i = 0
    bit = 1

    while (bit <= num):
        while i < bit and i + bit <= num:
            dp[i+bit] = dp[i] + 1 # new value dp[i+bit] depends on dp[i]
            i += 1
        i = 0 
        bit <<= 1 # bit = bit * 2
    return dp
