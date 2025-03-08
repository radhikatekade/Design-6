# Time complexity: O(nk + m(n+m/k))
# Space complexity: O(k(nk + m))
# where n = length of sentences, k = avg length of all sentences, m = num of times input is called

# Approach - Maintain a Trie storing children and sentences for every node. AddToTrie() maintains the count
# of times a sentence was typed. Input() keeps track of currNode and currSentence which takes care of three
# cases, when c == "#", when c != "#" and child of currNode, and when c != "#" and not child of currNode.

from typing import List, DefaultDict
import heapq
class TrieNode:
    def __init__(self):
        self.children = {}
        self.sentences = DefaultDict(int)

class AutocompleteSystem:
    def __init__(self, sentences: List[str], times: List[int]):
        self.root = TrieNode()
        for sentence, count in zip(sentences, times):
            self.add_to_trie(sentence, count)
            
        self.curr_sentence = []
        self.curr_node = self.root
        self.dead = TrieNode()
        
    def input(self, c: str) -> List[str]:
        if c == "#":
            curr_sentence = "".join(self.curr_sentence)
            self.add_to_trie(curr_sentence, 1)
            self.curr_sentence = []
            self.curr_node = self.root
            return []
        
        self.curr_sentence.append(c)
        if c not in self.curr_node.children:
            self.curr_node = self.dead
            return []
        
        self.curr_node = self.curr_node.children[c]
        items = [(val, key) for key, val in self.curr_node.sentences.items()]
        ans = heapq.nsmallest(3, items)
        return [item[1] for item in ans]

    def add_to_trie(self, sentence, count):
        node = self.root
        for c in sentence:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
            node.sentences[sentence] -= count


# Earlier approach - I tried using list for Trie's children, realized it was not taking care of spaces and
# hence giving an error (because ord(' ') - ord('a') negative.)
# class TrieNode:
#     def __init__(self):
#         self.children = [None for i in range(26)]
#         self.sentences = defaultdict(int)

# class AutocompleteSystem:

#     def __init__(self, sentences: List[str], times: List[int]):
#         self.root = TrieNode()
#         for sentence, count in zip(sentences, times):
#             self.insert(sentence, count)
#         self.curr_sentence = []
#         self.curr_node = self.root
#         self.dead = TrieNode()
    
#     def insert(self, sentence, count):
#         curr = self.root
#         for ch in sentence:
#             ch_int = ord(ch) - ord('a')
#             print(ch, ch_int)
#             if curr.children[ch_int] is None:
#                 curr.children[ch_int] = TrieNode()
#             curr = curr.children[ch_int]
#             curr.sentences[sentence] -= count        

#     def input(self, c: str) -> List[str]:
#         if c == "#":
#             string = "". join(self.curr_sentence)
#             self.insert(string, 1)
#             self.curr_sentence = []
#             self.curr_node = self.root
#             return []
        
#         self.curr_sentence.append(c)
#         c_int = ord(c) - ord('a')
#         if self.curr_node.children[c_int] is not None:
#             self.curr_node = self.dead
#             return []
        
#         self.curr_node = self.curr_node.children[c_int]
#         sentences = self.curr_node.sentences
#         heap = [(val, key) for key, val in sentences.items()]
#         ans = heapq.nsmallest(3, heap)
#         return [item[1] for item in ans]

        


# # Your AutocompleteSystem object will be instantiated and called as such:
# # obj = AutocompleteSystem(sentences, times)
# # param_1 = obj.input(c)