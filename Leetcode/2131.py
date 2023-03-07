from typing import List, Optional, Tuple
import pdb
import time

class Solution:
    def FindMirror(self, mirror_word: str, words: List[str], start: int, end: int, visited):
        if start > end:
            return (False, -1)
        
        mid = start + (end - start)//2
        if words[mid] == mirror_word:
            possible_match = mid
            while possible_match >= start and words[possible_match] == mirror_word:
                if possible_match not in visited:
                    return (True, possible_match)
                possible_match -= 1
            possible_match = mid
            while possible_match <= end and words[possible_match] == mirror_word:
                if possible_match not in visited:
                    return (True, possible_match)
                possible_match += 1
            return (False, -1)
        elif words[mid] < mirror_word:
            return self.FindMirror(mirror_word, words, mid + 1, end, visited)
        else:
            return self.FindMirror(mirror_word, words, start, mid -1, visited)

    def chunkify(self, words: List[str]):
        chunks = []
        visited = {}
        for wi in range(len(words)):
            w1 = words[wi]
            if wi in visited:
                continue
            mirror_word = w1[::-1]
            
            found = True
            search_from = wi + 1
            (found, mirror_idx) = self.FindMirror(mirror_word, words, search_from, len(words) - 1, visited)
            if found:
                #print(f'for {w1} found mirror word at index {mirror_idx}')
                visited[wi] = True
                visited[mirror_idx] = True
                chunks.append((w1, mirror_word))
            #print(f'visited after processing {words[:wi + 1]} is {sorted(visited.keys())} chunks is {chunks}')
        for wi in range(len(words)):
            if wi not in visited:
                w1 = words[wi]
                if w1[0] == w1[1]:
#                    print(f'self palindrome {w1}')
                    visited[wi] = True
                    chunks.append((w1,))
#        print(visited)
        return chunks

    def processChunks(self, chunks):
        self_palin = False
        size_palin = 0
        for chunk in chunks:
            if len(chunk) == 1 and not self_palin:
#                print(f'len = 1 {chunk}')
                self_palin = True
                size_palin += 2
            elif len(chunk) == 2:
#                print(f'len = 2 {chunk}')
                size_palin += 4
        return size_palin

    def createMap(self, words:List[str]):
        wmap = {}
        for wi in range(len(words)):
            word = words[wi]
            if word in wmap:
                wmap[word].append(wi)
            else:
                wmap[word] = [wi]

        return wmap


    def findPalindromesWithMap(self, words:List[str], wmap):
        total = 0
        visited = {}
        for wi in range(len(words)):
            if wi in visited:
                continue
            w = words[wi]
            wmap[w].pop(0)
            rw = w[::-1]
            ri = None
            if rw in wmap and len(wmap[rw]) > 0:
                ri = wmap[rw].pop(0)
                visited[wi] = True            
                visited[ri] = True
                total += 4
            #print(f'visited after processing {words[:wi + 1]} is {sorted(visited.keys())} total is {total} map is {wmap}')

        for wi in range(len(words)):
            if wi not in visited:
                if words[wi][0] == words[wi][1]:
                    total += 2
                    break
        return total

    def longestPalindrome(self, words: List[str]) -> int:
        words = sorted(words)
        print(words)
        #chunks = self.chunkify(words)
        #print(chunks)
        rmap = self.createMap(words)
        print(rmap)
        return self.findPalindromesWithMap(words, rmap)
        
if __name__ == '__main__':
    x = Solution()
    start = time.time()
    #words = ["lc","gg","cl"]
    #words = ["ab","ty","yt","lc","cl","ab"]
    #words = ["cc", "ll", "xx"]
    #words = ["em","pe","mp","ee","pp","me","ep","em","em","me"]
    #words = ["dd","aa","bb","dd","aa","dd","bb","dd","aa","cc","bb","cc","dd","cc"]
    words = ["mm","mm","yb","by","bb","bm","ym","mb","yb","by","mb","mb","bb","yb","by","bb","yb","my","mb","ym"]    
    #words = ["mb","mb","yb","by","yb","mb","ym"]
    #words = ["mb","yb","by","mb","yb","by","bb","yb","mb","ym"]
    print(x.longestPalindrome(words))
    end = time.time()
    elapsed = end - start
    print(f'time elapsed: {elapsed}')