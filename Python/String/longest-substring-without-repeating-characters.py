'''
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

'''

# Brute force O(n^2)
def lengthOfLongestSubstring_BruteForce(s):
    if len(s) == 1 or len(s) == 0: # edge case check
        return len(s)

    l, r, counter, res = 0, 0, 0, 0 # l = left pointer, r = right pointer

    while l < len(s):
        temp = set()
        r = l
        while r < len(s) and s[r] not in temp : # right pointer increasing until not unique
            temp.add(s[r])
            r += 1
        res = max(res, r-l)
    return res

# Optimized O(n) using sliding window
def lengthOfLongestSubstring(self, s):
    if len(s) == 1 or len(s) == 0: # edge case check
        return len(s)
    l = 0 # left pointer
    r = 0 # right pointer
    res = -1
    charset = set ()
    while ( l < len(s) and  r < len(s)):
        if s[r] not in charset: # if it is uniqe right pointer is increasing
            res = max( res, r-l+1)
            charset.add(s[r])
            r += 1
        else: # else left pointer is increasing and remove s[l] from the set
            if s[l] in charset:
                charset.remove(s[l])
            l += 1
    return res if res != -1 else 0
