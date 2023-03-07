from typing import List, Optional, Tuple, Dict
import deque
import pdb
import time

class Solution:
    def altSolution(self, start: str, end: str, bank: List[str]) -> int:
        queue = deque([(start, 0)])
        seen = {start}
        
        while queue:
            node, steps = queue.popleft()
            if node == end:
                return steps

            for c in "ACGT":
                for i in range(len(node)):
                    neighbor = node[:i] + c + node[i + 1:]
                    if neighbor not in seen and neighbor in bank:
                        queue.append((neighbor, steps + 1))
                        seen.add(neighbor)

        return -1
    def isOneFlipAway(self, one: str, two: str) -> bool:
        flips = 0
        for idx in range(len(one)):
            ol = one[idx]
            tl = two[idx]
            if ol != tl:
                flips += 1
                if flips > 1:
                    return False
        return flips == 1

    def createGraphForBank(self, effectiveBank: List[str]) -> List[List[int]]:
        # Represent graph as an adjacency list storing list of vertices one edit distance
        # away from a given vertex.
        graph = [[] for i in range(len(effectiveBank))]
        print(effectiveBank)
        for i1, w1 in enumerate(effectiveBank):
            for i2, w2 in enumerate(effectiveBank):
                if self.isOneFlipAway(w1, w2):
                    graph[i1].append(i2)
        return graph

    def traverseGraphFrom(self, source: int, graph: List[List[int]], visited: Dict[int, bool], minDistanceFromSource: List[int]):
        for vertex in graph[source]:
            visited[vertex] = True
            if minDistanceFromSource[vertex] == -1 or minDistanceFromSource[source] + 1 < minDistanceFromSource[vertex]:
                minDistanceFromSource[vertex] = minDistanceFromSource[source] + 1
                self.traverseGraphFrom(vertex, graph, visited, minDistanceFromSource)
            visited[vertex] = False

    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if len(bank) == 0:
            return -1
        target_idx = 0
        effectiveBank = [startGene] + bank
        try:
            target_idx = effectiveBank.index(endGene)
        except Exception as e:
            return -1
        connections = self.createGraphForBank(effectiveBank)
        minDistanceFromSource = [-1 for i in range(len(effectiveBank))]
        if len(minDistanceFromSource) > 0:
            minDistanceFromSource[0] = 0
        self.traverseGraphFrom(0, connections, {}, minDistanceFromSource)
        print(minDistanceFromSource)
        target_idx = effectiveBank.index(endGene)
        return minDistanceFromSource[target_idx]

if __name__ == '__main__':
    x = Solution()
    start = time.time()
    startGene = "AACCGGTT"
    endGene = "AACCGGTA"
    #endGene = "AAACGGTA"
    #bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
    bank = ["AACCGGTA"]
    print(x.minMutation(startGene, endGene, bank))
    end = time.time()
    elapsed = end - start
    print(f'time elapsed: {elapsed}')
