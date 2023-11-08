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
    end: int
    second_last: int
    visited: frozenset[int]

    def __init__(self, start, second_last, end, visited) -> None:
        self.start = start
        self.second_last = second_last
        self.end = end
        self.visited = frozenset(visited)

    def __str__(self):
        return f"path start: {self.start}, second last: {self.second_last} end: {self.end}, nodes: {self.visited}"

    def __repr__(self):
        return f"path start: {self.start}, second last: {self.second_last}, end: {self.end}, nodes: {self.visited}"

class Solution:
    def findCycleOfLength(self, connections: Dict[int, set[int]],
                          known_paths_start: Dict[int, set[Path]],
                          n: int, length: int):
        for starting in range(n):
            print(locals())
            all_paths = []
            if length > 1 and starting in known_paths_start:
                all_paths = known_paths_start[starting]

                paths_to_add = set()
                while len(all_paths) > 0:
                    path = all_paths.pop()
                    new_vertices = set()

                    # path contains all points we are on after length - 1 steps,
                    # given that we started from 'starting'.
                    if len(path.visited) != length:
                        print(f"Invariant violated, path length is {len(path.visited)} while given length is {length}")

                    last_vertex = path.end
                    if last_vertex in connections:
                        for conn in connections[last_vertex]:
                            if path.second_last != conn and conn in path.visited:
                                return True
                            new_vertices.add(conn)
                
                    # We have now found a bunch of new vertices for the path.
                    # Add the new paths to 'known_paths_start'.
                    for vertex in new_vertices:
                        s = path.start
                        second_last = path.end
                        e = vertex
                        v = set(path.visited)
                        v.add(vertex)
                        v = frozenset(v)
                        paths_to_add.add(Path(s, second_last, e, v))
                
                if paths_to_add:
                    known_paths_start[starting] = paths_to_add
                else:
                    del known_paths_start[starting]
            # No prior path information.
            elif length == 1 and starting in connections:
                for conn in connections[starting]:
                    if starting not in known_paths_start:
                        known_paths_start[starting] = {Path(starting, starting, conn, frozenset({starting, conn}))}
                    else:
                        known_paths_start[starting].add(Path(starting, starting, conn, frozenset({starting, conn})))
        return False

    def findShortestCycle(self, n: int, edges: List[List[int]]) -> int:
        connections = {}
        for edge in edges:
            if edge[0] in connections:
                connections[edge[0]].add(edge[1])
            else:
                connections[edge[0]] = {edge[1]}
            if edge[1] in connections:
                connections[edge[1]].add(edge[0])
            else:
                connections[edge[1]] = {edge[0]}

        known_paths = {}
        for i in range(1, n + 1):
            print('\nlength = ', i)
            if self.findCycleOfLength(connections, known_paths, n, i):
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