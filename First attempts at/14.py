#!/usr/bin/env python
from typing import List
import time

class TrieNode:
    def __init__(self):
        self.val = ''
        self.count = 0
        self.next = None

class Trie:
    def __init__(self):
        self.trie = TrieNode()

    def MatchStr(self, some_str: str):
        idx = 0
        trie = self.trie
        while idx < len(some_str) and (trie.val == '' or trie.val == some_str[idx]):
            #print(f'char {some_str[idx]} trie.val = {trie.val}')
            if trie.val == '':
                trie.val = some_str[idx]
                trie.next = TrieNode()
            trie.count += 1
            trie = trie.next
            idx += 1
        return

    def ReturnTrieNodeWithCount(self, count: int):
        trie = self.trie
        constructed = ''
        while trie.count >= count and trie.next != None:
            constructed = constructed + trie.val
            #print(trie.val)
            trie = trie.next
            continue
        return constructed

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        trie = Trie()
        for astr in strs:
            trie.MatchStr(astr)

        return trie.ReturnTrieNodeWithCount(len(strs)) 
        
if __name__ == '__main__':
    x = Solution()
    start = time.time()
    strs = ["flower","flow","flight"]
    print(x.longestCommonPrefix(strs))
    end = time.time()
    elapsed = end - start
    print (f'time elapsed = {elapsed}')
