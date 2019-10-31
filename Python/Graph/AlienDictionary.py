'''
There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. You receive a list of non-empty words from the dictionary, where words are sorted lexicographically by the rules of this new language. Derive the order of letters in this language.

Example 1:

Input:
[
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]

Output: "wertf"
Example 2:

Input:
[
  "z",
  "x"
]

Output: "zx"
Example 3:

Input:
[
  "z",
  "x",
  "z"
]

Output: ""

Explanation: The order is invalid, so return "".
Note:

You may assume all letters are in lowercase.
You may assume that if a is a prefix of b, then a must appear before b in the given dictionary.
If the order is invalid, return an empty string.
There may be multiple valid order of letters, return any one of them is fine.
Accepted

'''

# Approach:  break it into two parts :
# 1) Build graph
# 2) Topological sort
# Time complexity build graph O(n) &  BFS O(V+E)

class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        if not words:
            return ""
        graph = collections.defaultdict(set)
        inDegreeMap = collections.defaultdict(int)
        BuildGraph(words, graph, inDegreeMap)
        return BFSTopologicalSort(words, graph, inDegreeMap)

def BuildGraph(words, graph, inDegreeMap):
    for word in words:
        for c in word: inDegreeMap[c] = 0

    for i in range(len(words)-1):
        curWord, nextWord = words[i], words[i+1]
        minLen = min(len(curWord), len(nextWord))

        """according to given dictionary with specified order,
        traverse every pair of words then put each pair into
        graph map to build the graph, and then update inDegree map
        for every "nextChar" (increase their inDegree by 1 every time)"""
        for j in range(minLen):
            curChar, nextChar = curWord[j], nextWord[j]

            if curChar == nextChar: continue
            curCharSet = graph[curChar]

            if nextChar not in curCharSet:   # checking duplicate cases such as ["za","zb","ca","cb"] input ->output "azbc" or "abzc"
                curCharSet.add(nextChar)
                inDegreeMap[nextChar] += 1
            """ determine the order of characters ony by
            first different pair of characters so we cannot
            add relationship by the rest of character """
            break

def BFSTopologicalSort(words, graph, inDegreeMap):
    res, queue = "", []
    for key in inDegreeMap.keys():
        if inDegreeMap[key] == 0: queue.append(key)

    while queue:
        curChar = queue.pop(0)
        res += curChar
        if curChar not in graph: continue

        for nextChar in graph[curChar]:
            inDegreeMap[nextChar] -= 1
            if inDegreeMap[nextChar] == 0:
                queue.append(nextChar)

    for  char in inDegreeMap:
            if inDegreeMap[char] > 0: # if there is a prerequisite that is not visited, return false
                return ''             # e.g. ["dj","dd","jd"] => output ''
    return  res

'''
More Test cases
Input ["z","z"]
Output "z"

Input ["za","zb","ca","cb"]
Output "abzc"

Input ["ri","xz","qxf","jhsguaw","dztqrbwbm","dhdqfb","jdv","fcgfsilnb","ooby"]
Output ""
'''
