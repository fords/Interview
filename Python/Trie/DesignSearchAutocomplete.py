"""
Design a search autocomplete system for a search engine. Users may input a sentence (at least one word and end with a special character '#'). For each character they type except '#', you need to return the top 3 historical hot sentences that have prefix the same as the part of sentence already typed. Here are the specific rules:

The hot degree for a sentence is defined as the number of times a user typed the exactly same sentence before.
The returned top 3 hot sentences should be sorted by hot degree (The first is the hottest one). If several sentences have the same degree of hot, you need to use ASCII-code order (smaller one appears first).
If less than 3 hot sentences exist, then just return as many as you can.
When the input is a special character, it means the sentence ends, and in this case, you need to return an empty list.
Your job is to implement the following functions:

The constructor function:

AutocompleteSystem(String[] sentences, int[] times): This is the constructor. The input is historical data. Sentences is a string array consists of previously typed sentences. Times is the corresponding times a sentence has been typed. Your system should record these historical data.

Now, the user wants to input a new sentence. The following function will provide the next character the user types:

List<String> input(char c): The input c is the next character typed by the user. The character will only be lower-case letters ('a' to 'z'), blank space (' ') or a special character ('#'). Also, the previously typed sentence should be recorded in your system. The output will be the top 3 historical hot sentences that have prefix the same as the part of sentence already typed.


Example:
Operation: AutocompleteSystem(["i love you", "island","ironman", "i love coding"], [5,3,2,2])
The system have already tracked down the following sentences and their corresponding times:
"i love you" : 5 times
"island" : 3 times
"ironman" : 2 times
"i love coding" : 2 times
Now, the user begins another search:

Operation: input('i')
Output: ["i love you", "island","i love coding"]
Explanation:
There are four sentences that have prefix "i". Among them, "ironman" and "i love coding" have same hot degree. Since ' ' has ASCII code 32 and 'r' has ASCII code 114, "i love coding" should be in front of "ironman". Also we only need to output top 3 hot sentences, so "ironman" will be ignored.

Operation: input(' ')
Output: ["i love you","i love coding"]
Explanation:
There are only two sentences that have prefix "i ".

Operation: input('a')
Output: []
Explanation:
There are no sentences that have prefix "i a".

Operation: input('#')
Output: []
Explanation:
The user finished the input, the sentence "i a" should be saved as a historical sentence in system. And the following input will be counted as a new search.

Note:
The input sentence will always start with a letter and end with '#', and only one blank space will exist between two words.
The number of complete sentences that to be searched won't exceed 100. The length of each sentence including those in the historical data won't exceed 100.
Please use double-quote instead of single-quote when you write test cases even for a character input.
Please remember to RESET your class variables declared in class AutocompleteSystem, as static/class variables are persisted across multiple test cases. Please see here for more details.
"""
import heapq

class Trie:
    def __init__(self):
        """Init Trie"""
        self.char_map, self.search_count = {}, 0

    def insert(self, sentence, count):
        """Add to Trie"""
        current = self
        for char in sentence:
            if char not in current.char_map:
                current.char_map[char] = Trie()
            current = current.char_map[char]
        current.search_count += count

class AutoCompleteSystem:
    def __init__(self, sentences, times):
        """Init AutoCompleteSystem"""
        self.trie_root, self.curr_input, self.hot_sentences = Trie(), [], []
        for search_hist in zip(sentences, times):  # Build Trie
            self.trie_root.insert(*search_hist)

    def _search_prefix(self, prefix):
        """Search for input query in Trie and return top 3 hot sentences
        sorted by hot degree
        Worst Case Time: O(d) where d is the max depth of the Trie"""
        max_heap, current = [], self.trie_root

        for char in prefix: # Navigate to prefix depth
            if char in current.char_map:
                current = current.char_map[char]
            else: # Prefix not in Trie, return empty array
                return max_heap

        def dfs_helper(node, partial_search):
            if node.search_count:
                max_heap.append((-node.search_count,"".join(partial_search)))
            for key in node.char_map.keys():
                dfs_helper(node.char_map[key], partial_search + key)

        dfs_helper(current, [prefix])

        heapq.heapify(max_heap)
        return [heapq.heappop(max_heap)[1] for _ in range(3) if len(max_heap)]

    def input(self, char):
        """Process user input"""
        if char == '#':
            self.trie_root.insert("".join(self.curr_input), 1)
            self.curr_input = []
            return []
        else:
            self.curr_input.append(char)
        return self._search_prefix("".join(self.curr_input))

sentences = ["i love you", "island","ironman", "i love coding"]
times = [5,3,2,2]
searchSystem = AutoCompleteSystem(sentences, times)
print(searchSystem.input('i'))
print(searchSystem.input(' '))
print(searchSystem.input('a'))
print(searchSystem.input('#'))
print(searchSystem.input('is'))

sentences = ["A","to", "tea", "ted", "ten", "i", "in", "inn"]
times = [15, 7, 3, 4, 12, 11, 5, 9]
searchSystem = AutoCompleteSystem(sentences, times)
print(searchSystem.input(''))
print(searchSystem.input('t'))
print(searchSystem.input(' '))
print(searchSystem.input('#'))
print(searchSystem.input('i'))
print(searchSystem.input('#'))
print(searchSystem.input('t '))
