'''
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
Note:

If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.
'''
import copy

# Initial approach brute force O(n^2)
def minwindow_bruteforce(s,t):
    dic = {}
    for char in t: # Count all characters in t
        dic[char] = dic.get(char,0) + 1
    ans = [-1,len(s)]
    for i in range(len(s)):
         j = i
         temp = copy.deepcopy(dic)
         count =  0
         while j < len(s): # Do loop in s until find all characters in t
            if s[j] in temp and temp[s[j]] > 0:
                temp[s[j]] -= 1
                count += 1

            if count == len(t): # if found all characters, update answer
                if j-i < ans[1] - ans[0]:
                    ans = [i,j]
                break
            j += 1

    if ans[0] != -1: # return answer if there is valid answer
        return s[ans[0]:ans[1]+1]
    else: # if no answer is found return empty string
        return ''

print "Test output: ",minwindow_bruteforce("this is a test string", "sttr") ,"**** Expected: t str"

''' # Initial brute force working with unique val.  Didn't work with duplicate characters such as s= "aacfd" t = "acd"
        charset = set()
        for char in t:
            charset.add(char)
        start, end = 0 , len(s)
        for i in range(len(s)):
            count = 0
            for j in range(i,len(s)):
                if s[j] in charset:
                    count += 1
                if count == len(t):
                    print 'true'
                    if end - start > j - i :
                        end, start = j , i
                        # print 'end start' ,end, start
                    break
        return s[start:end+1] if end != len(s) else ''
'''


# Optimized O(n) approach
# Sliding window : two pointers
def minwindow(s,t):
    target_count = {}
    for ch in t:
        target_count[ch] = target_count.get(ch,0) + 1

    count = 0 # count of target character in string
    start = 0 # answer for left index of string
    end = float('inf') # answer for right index of string
    l = 0  # left pointer
    r = 0 # right pointer

    while r < len(s):
        ch = s[r]
        if ch in target_count and target_count[ch] > 0:
            count += 1
        if ch in target_count:
            target_count[ch] -= 1

        if count == len(t): # if found all characters in s
            while (s[l] in target_count and target_count[s[l]] < 0) or s[l] not in target_count:
                if s[l] in target_count:
                    target_count[s[l]] += 1 # restore the count value in dict
                l += 1

            if r - l < end - start: # keep minium index values as answer
                start, end = l , r
            if s[l] in target_count: # restore the count value in dict
                target_count[s[l]] += 1
            count -= 1 # since left pointer is incrementing, reduce the count of character
            l += 1
        r += 1
    return s[start:end+1] if end != float('inf') else ''


# O(n) another approach: for loop in sliding window: Detailed explanation
def minWindow(s, t):
    need = collections.Counter(t)            #hash table to store char frequency
    missing = len(t)                         #total number of chars we care
    start, end = 0, 0
    i = 0
    for j, char in enumerate(s, 1):          #index j from 1
        if need[char] > 0:
            missing -= 1
        need[char] -= 1
        if missing == 0:                     #match all chars
            while i < j and need[s[i]] < 0:  #remove chars to find the real start
                need[s[i]] += 1
                i += 1
            need[s[i]] += 1                  #make sure the first appearing char satisfies need[char]>0
            missing += 1                     #we missed this first char, so add missing by 1
            if end == 0 or j-i < end-start:  #update window
                start, end = i, j
            i += 1                           #update i to start+1 for next window
    return s[start:end]
