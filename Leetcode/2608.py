from typing import List, Optional, Tuple, Dict
from heapq import heappop, heappush, heapify
import copy
import pdb
import ast
import sys
from functools import cmp_to_key
import time

class Path:
    start: int
    last_edge: Tuple[int, int]
    visited: frozenset[int]

    def __init__(self, start, edge, visited) -> None:
        self.start = start
        self.last_edge = edge
        self.visited = frozenset(visited)

    def __str__(self):
        return f"path start: {self.start}, last edge: {self.last_edge}, nodes: {self.visited}"

    def __repr__(self):
        return f"path start: {self.start}, last edge: {self.last_edge}, nodes: {self.visited}"

class Solution:
    def findCycle(self, known_paths: set[Path], connections: Dict[int, set[int]], n: int, visited: set[set[int]]):
        all_paths = known_paths
        paths_to_add = set()

        while len(all_paths) > 0:
            path = all_paths.pop()
            #print(f'processing path {path}')
            new_vertices = set()

            last_edge = path.last_edge
            first_vertex = last_edge[0]
            last_vertex = last_edge[1]
            if last_vertex in connections:
                for conn in connections[last_vertex]:
                    if first_vertex == conn:
                        continue
                    if conn in path.visited:
                        return True
                    new_vertices.add(conn)

            # We have now found a bunch of new vertices for the path.
            # Add the new paths to 'known_paths_start'.
            for vertex in new_vertices:
                v = set(path.visited)
                v.add(vertex)
                if v in visited:
                    continue
                visited.add(frozenset(v))
                v = frozenset(v)
                s = path.start
                last_edge = (path.last_edge[1], vertex)
                paths_to_add.add(Path(s, last_edge, v))

        known_paths.clear()
        for path in paths_to_add:
            known_paths.add(path)
        return False

    def findShortestCycle(self, n: int, edges: List[List[int]]) -> int:
        known_paths = set()
        connections = {}
        visited = set()
        for edge in edges:
            if edge[0] in connections:
                connections[edge[0]].add(edge[1])
            else:
                connections[edge[0]] = {edge[1]}
            if edge[1] in connections:
                connections[edge[1]].add(edge[0])
            else:
                connections[edge[1]] = {edge[0]}

        for edge in edges:
            source = edge[0]
            dest = edge[1]
            known_paths.add(Path(source, (edge[0], edge[1]), frozenset({edge[0], edge[1]})))
            known_paths.add(Path(dest, (edge[1], edge[0]), frozenset({edge[0], edge[1]})))

        for i in range(2, n + 1):
            if len(known_paths) == 0:
                return -1
            print(f'\nlength = {i} number of paths = {len(known_paths)}')
            for path in known_paths:
                print(f'length of path = {len(path.visited)}')
                break
            if self.findCycle(known_paths, connections, n, visited):
                return i
        return -1

if __name__ == '__main__':
    x = Solution()
    start = time.time()
    with open('2608_tc.text', 'r') as f:
        n = ast.literal_eval(f.readline())
        #print(n)
        edges = ast.literal_eval(f.readline())
        #print(edges)
        print(x.findShortestCycle(n, edges))
    end = time.time()
    elapsed = end - start
    print(f'time elapsed: {elapsed}')