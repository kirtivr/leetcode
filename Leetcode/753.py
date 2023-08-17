from typing import List, Optional, Tuple, Dict
from heapq import heappop, heappush, heapify
import pdb
import ast
import sys
from functools import cmp_to_key
import time

class Solution:
    def __init__(self):
        self.string = ''

    def createPermutations(self, n, k):
        all_chars = []
        for i in range(0, k, 1):
            all_chars.append(str(i))

        perms = [ch for ch in all_chars]
        for i in range(n - 1):
            N = len(perms)
            for j in range(N):
                perm = perms.pop(0)
                for c in all_chars:
                    new_perm = c + perm
                    perms.append(new_perm)

        return perms

    def tryLinkingAllPossiblePermutationsStartingFrom(self, to_visit, connections, N, visited, fullString):
        #print(f'fullString = {fullString} len(visited) = {len(visited)} N = {N}')
        if self.string:
            return
        a = ''
        if not fullString:
            a = to_visit
        elif len(to_visit) == 1:
            a = fullString + to_visit
        else:
            # Only add the last character of to_visit, because fullString's suffix is the same as the last character's prefix.
            a = fullString + to_visit[-1]

        visited[to_visit] = True

        if len(a) == N:
            #print(f'string = {a} N = {N}')
            if not self.string or len(a) < len(self.string):
                self.string = a
            del(visited[to_visit])
            return

        for neighbor in connections[to_visit]:
            if neighbor in visited:
                continue
            #print(f'string = {a} unvisited neighbor = {neighbor}')
            self.tryLinkingAllPossiblePermutationsStartingFrom(neighbor, connections, N, visited, a)

        del(visited[to_visit])

    def crackSafe(self, n, k) -> int:
        # There are k total numbers.
        # Create all permutations of up to size n.

        perms = set(self.createPermutations(n, k))
        #print(perms)
        # Neighboring permutations are those that:
        #  ex. 5643 and 643X, X564
        # So all numbers that have the last N - 1 numbers of the input number as its prefix,
        # or the first N - 1 number of the input number as its suffix are its neighbors.

        # We can just concatenate arbitrary characters from the alphabet to construct all neighbors we want for an
        # input number.
        connections = {}
        all_chars = []
        for i in range(0, k, 1):
            all_chars.append(str(i))
        for perm in perms:
            suffix = perm[1:]

            sn = []
            for ch in all_chars:
                sn.append(suffix + ch)
            connections[perm] = sn
        #print(perms)
        #print(connections)
        for perm in perms:
            visited = {}
            optimal_sz = n + len(perms) - 1
            self.tryLinkingAllPossiblePermutationsStartingFrom(perm, connections, optimal_sz, visited, "")
            if self.string:
                break

        return self.string

if __name__ == '__main__':
    x = Solution()
    start = time.time()
    with open('753_tc.text', 'r') as f:
        n = ast.literal_eval(f.readline())
        #print(n)
        k = ast.literal_eval(f.readline())
        #print(edges)
        out = x.crackSafe(n, k)
        print(f"len(string) = {len(out)} string = {out}")
    end = time.time()
    elapsed = end - start
    print(f'time elapsed: {elapsed}')