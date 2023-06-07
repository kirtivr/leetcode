from typing import List, Optional, Tuple, Dict
from heapq import heappop, heappush, heapify, nsmallest
import pdb
import ast
import sys
from functools import cmp_to_key
import time

#Here are the specific rules:

#The hot degree for a sentence is defined as the number of times a user typed the exactly same sentence before.
#The returned top 3 hot sentences should be sorted by hot degree (The first is the hottest one). If several sentences have the same hot degree, use ASCII-code order (smaller one appears first).
#If less than 3 hot sentences exist, return as many as you can.
#When the input is a special character, it means the sentence ends, and in this case, you need to return an empty list.
class TrieNode:
    def __init__(self, letter, parent_node):
        self.letter = letter
        self.terminal = False
        self.count = 0
        self.parent_node = parent_node
        # Note that space is a valid continuation.
        self.continuations = [None for i in range(27)]
        self.sorted_continuations = []

    def get_sorted_matches(self):
        return [pair[1] for pair in self.sorted_continuations][:3]

    def cmp_matches(self, a, b):
        if a[0] > b[0] or (a[0] == b[0] and a[1] < b[1]):
            return -1
        elif a == b:
            return 0
        else:
            return 1

    def push_to_heap(self, count, sentence):
        found = False
        #print(f'pushing {sentence}')
        for i in range(len(self.sorted_continuations)):
            if self.sorted_continuations[i][1] == sentence:
                found = True
                self.sorted_continuations[i][0] = count
                break            
        
        if found:
            self.sorted_continuations.sort(key=cmp_to_key(self.cmp_matches))
        else:
            self.sorted_continuations.append([count, sentence])
            self.sorted_continuations.sort(key=cmp_to_key(self.cmp_matches))
        self.sorted_continuations = self.sorted_continuations[:3]
        #print(f'sorted continuations = {self.sorted_continuations}')

    def bubble_up(self, count, sentence):
        current = self.parent_node
        while current != None:
            current.push_to_heap(count, sentence)
            current = current.parent_node

    def __repr__(self):
        out = f'{self.letter} : ['
        for continuation in self.continuations:
            #print(continuation)
            if continuation is None:
                continue
            out += f'\t\t\n{continuation}'
        out += ']'
        return out

class Trie:
    def __init__(self, sentences: List[str], times: List[int]):
        self.root = TrieNode('', None)
        self.sentence_to_node_map = {}
        self.current_node = self.root
        self.construct_trie(sentences, times)

    def construct_trie(self, sentences: List[str], times: List[int]):        
        for idx, sentence in enumerate(sentences):
            #print(f'adding {sentence} to trie\n\n')
            count = times[idx]
            self.add_to_trie(sentence, count)

    def add_to_trie(self, sentence, count):
        current_node = self.root
        
        for lidx, letter in enumerate(sentence):
            #print(f'i = {lidx} c = {letter}')
            # If there is a valid continuation, follow it.
            current_node = self.lookup_char(letter, current_node)
            # Don't need to do anything unless this is the terminal node.
            if lidx == len(sentence) - 1:
                current_node.terminal = True
                current_node.count += count
                current_node.push_to_heap(current_node.count, sentence)

                current_node.bubble_up(current_node.count, sentence)

    def add_current_looked_up_to_trie(self, sentence):
        if self.current_node.terminal:
            self.current_node.count += 1
        else:
            self.current_node.terminal = True
            self.current_node.count = 1
        #print(f'adding {sentence} terminal? { self.current_node.terminal} count = {self.current_node.count}')
        self.current_node.push_to_heap(self.current_node.count, sentence)
        self.current_node.bubble_up(self.current_node.count, sentence)

    def reset(self):
        self.current_node = self.root

    def lookup_trie(self, letter):
        current = self.lookup_char(letter, self.current_node)
        self.current_node = current
        return current.get_sorted_matches()

    def lookup_char(self, letter, current):
        #print(f'letter = {letter}')
        if letter == ' ':
            if not current.continuations[26]:
                current.continuations[26] = TrieNode(letter, current)
            current = current.continuations[26]
        elif not current.continuations[ord(letter) - ord('a')]:
            current.continuations[ord(letter) - ord('a')] = TrieNode(letter, current)
            current = current.continuations[ord(letter) - ord('a')]
        else:
            current = current.continuations[ord(letter) - ord('a')]
        return current

    def __repr__(self):
        return f'{self.root}'

class AutocompleteSystem:
    def __init__(self, sentences: List[str], times: List[int]):
        self.trie = Trie(sentences, times)
        #print(self.trie)
        self.sentence = ''

    def input(self, c: str) -> List[str]:
        #print(f'c = {c}')
        if c[0] == '#':
            # Input is terminated, push into trie.
            if self.sentence != '':
                self.trie.add_current_looked_up_to_trie(self.sentence)
            self.trie.reset()
            self.sentence = ''
            #print(self.trie)
            return []
        else:
            #print(f'{self.sentence} : {self.trie.lookup_trie(c[0])}')
            self.sentence += c[0]
            return self.trie.lookup_trie(c[0])
            

# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)

if __name__ == '__main__':
    start = time.time()
    #cmds = ["AutocompleteSystem", "input", "input", "input", "input"]
    #args = [[["i love you", "island", "iroman", "i love leetcode"], [5, 3, 2, 2]], ["i"], [" "], ["a"], ["#"]]
    cmds = ["AutocompleteSystem","input","input","input","input","input","input","input","input","input","input","input","input"]
    args = [[["i love you","island","iroman","i love leetcode"],[5,3,2,2]],["i"],[" "],["a"],["#"],["i"],[" "],["a"],["#"],["i"],[" "],["a"],["#"]]
    auto_s = AutocompleteSystem(args[0][0], args[0][1])
    input = args[1:]
    for i in input:
        print(auto_s.input(i))
    end = time.time()
    elapsed = end - start
    print(f'time elapsed: {elapsed}')