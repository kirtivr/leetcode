from heapq import heappop, heappush, heapify
from dataclasses import dataclass, field
from typing import Any

class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        table = {}

        T = len(t)
        S = len(s)
        
        for i in range(T):
            table[t[i]] = 1 if t[i] not in table else table[t[i]] + 1

        oldT = dict(table)
        indices = []        
        for i in range(S):
            if s[i] in table:
                indices.append(i)

        seen = {key : [] for key in table.keys()}
        #print(seen)
        indices_added = []
        invalid_indices = {}
        out = None

        for i in indices:
            #print(f'\ns = {s} processed = {s[:i + 1]} remaining = {s[i + 1 :]} i = {i} incoming = {s[i]} table = {table}')
            # Either evict the earliest index or add s[i] to seen.
            if s[i] not in table:
                # Evict.
                evicted = seen[s[i]][0]
                #print(f'evicting {s[i]} at index {evicted}')
                seen[s[i]].pop(0)
                invalid_indices[evicted] = True
                seen[s[i]].append(i)
                indices_added.append(i)
                continue

            seen[s[i]].append(i)
            indices_added.append(i)

            table[s[i]] -= 1
            if table[s[i]] == 0:
                del table[s[i]]
                if len(table) == 0:
                    # Find the first valid index.
                    first = None
                    for j in range(len(indices_added)):
                        if indices_added[j] not in invalid_indices:
                            first = indices_added[j]
                            break
                    indices_added = indices_added[j + 1 :]
                    seen[s[first]].pop(0)

                    #print(f'first = {first} i = {i} invalid = {invalid_indices} candidate {s[first : i + 1]}')
                    if out:
                        if i - first + 1 < len(out):
                            out = s[first : i + 1]
                    else:
                        out = s[first : i + 1]

                    if s[first] not in table:
                        table[s[first]] = 1
                    else:
                        table[s[first]] += 1
                    
                    continue
            
        return out if out is not None else ""
                
                

if __name__ == '__main__':
    S = "ADOBECODEBANC"
    T = "ABC"
    '''S = "acbbaca"
    T = "aba"
    S = "cabefgecdaecf"
    T = "cae"
    S = "bdab"
    T = "ab"
    S = "aaflslflsldkalskaaa"
    T = "aaa"'''
    
    S = "adobecodebancbbcaa"
    T = "abc"
    print(Solution().minWindow(S,T))
            
                
                
            
                 
