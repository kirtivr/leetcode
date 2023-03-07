from typing import List, Optional, Tuple, Dict
from heapq import heappop, heappush, heapify
import pdb
import ast
import sys
from functools import cmp_to_key
import time

class Solution:
    def recursivelyColorNeighborsOfNode(self, node, nodes, neighbors, visited, colors):
        #print(f'\nrecursively coloring neighbor {node}')
        nc = max((colors[node] + 1) % 5, 1)

        for j in range(len(neighbors[node])):
            neighbor = neighbors[node][j]
            #print(f'neighbor = {neighbor}')
            if visited[neighbor]:
                if colors[neighbor] == colors[node]:
                    return False
                continue

            initial_color = nc
            colors[neighbor] = nc
            #print(f'colors = {colors} picked {colors[node]} for {node}, {nc} for neighbor {neighbor}')

            res = False
            while not res:
                visited[neighbor] = True
                #print(f'calling color neighbor for node {neighbor}')
                res = self.recursivelyColorNeighborsOfNode(neighbor, nodes, neighbors, visited, colors)
                # Try a different color
                if not res:
                    visited[neighbor] = False
                    nc = max((nc + 1) % 5, 1)
                    if nc == initial_color:
                        break
                    colors[neighbor] = nc

            if not res:
                return False

        return True

    def assignColors(self, nodes, neighbors, visited, colors):
        for i in range(len(nodes)):
            pick_color = 1
            to_visit = nodes[i]
            if visited[to_visit]:
                continue
            #print(f'\nvisiting {to_visit}')

            colors[to_visit] = pick_color
            res = False
            visited[to_visit] = True 

            while not res and pick_color != 0:
                res = self.recursivelyColorNeighborsOfNode(to_visit, nodes, neighbors, visited, colors)
                if not res:
                    pick_color = (pick_color + 1) % 5
                    colors[to_visit] = pick_color

        return True

    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        visited = {i: False for i in range(n)}
        colors = [-1 for i in range(n)]
        neighbors = {i: [] for i in range(n)}

        for i in range(len(paths)):
            (a, b) = paths[i]
            neighbors[a - 1].append(b - 1)
            neighbors[b - 1].append(a - 1)

        nodes = sorted(neighbors.keys(), key= lambda k : len(neighbors[k]), reverse=True)
        colors[nodes[0]] = 1
        self.assignColors(nodes, neighbors, visited, colors)
        return colors

if __name__ == '__main__':
    x = Solution()
    start = time.time()
    with open('1042_tc.text', 'r') as f:
        n = ast.literal_eval(f.readline())
        #print(n)
        paths = ast.literal_eval(f.readline())
        #print(edges)
        print(x.gardenNoAdj(n, paths))
    end = time.time()
    elapsed = end - start
    print(f'time elapsed: {elapsed}')