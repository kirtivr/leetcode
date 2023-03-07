from typing import List, Optional, Tuple, Dict
import pdb
import ast
import sys
from functools import cmp_to_key
import time



class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        connections = [[] for i in range(n)]
        for edge in edges:
            u = edge[0] - 1
            v = edge[1] - 1
            connections[u].append(v)
            connections[v].append(u)

        members = {}
        for i in range(len(connections)):
            members[i] = {}
            for j in range(len(connections[i])):
                members[i][connections[i][j]] = True

        num_connections = [i for i in range(len(connections))]
        def sortByConnectionCount(index: int) -> int:
            return len(connections[index])
        num_connections = sorted(num_connections, key=sortByConnectionCount)
        for ci in range(len(connections)):
            connections[ci] = sorted(connections[ci], key=sortByConnectionCount)
        #print(f'connections = {connections}')
        #print(f'num_connections sorted = {num_connections}')
        visited = {}
        min_degree = float("inf")
        for min_v in num_connections:
            connections_of_min = connections[min_v]
            for next_min_v in connections_of_min:
                if (min_v, next_min_v) in visited:
                    continue
                visited[(min_v, next_min_v)] = True
                visited[(next_min_v, min_v)] = True
                connections_of_nmv = connections[next_min_v]
                #print(f'connections of {min_v}: {connections[min_v]}')
                #print(f'connections of {next_min_v}: {connections[next_min_v]}')
                for cnmv in connections_of_nmv:
                    # We are looking for a third point.
                     if cnmv == min_v or (cnmv, min_v) in visited or (cnmv, next_min_v) in visited:
                        continue
                    #print(f'checking common connections of {min_v} {next_min_v} testing {cnmv}')
                     if cnmv in members[min_v]:
                        #print(f'its a match. len(connections[min_v]) = {len(connections[min_v])} len(connections[next_min_v]) = {len(connections[next_min_v])} len(connections[cnmv]) = {len(connections[cnmv])}')
                        degree = len(connections[min_v]) + len(connections[next_min_v]) + len(connections[cnmv]) - 6
                        min_degree = min(min_degree, degree)
        return -1 if min_degree == float("inf") else min_degree
if __name__ == '__main__':
    x = Solution()
    start = time.time()
    with open('1761_tc.text', 'r') as f:
        n = ast.literal_eval(f.readline())
        #print(n)
        edges = ast.literal_eval(f.readline())
        #print(edges)
        print(x.minTrioDegree(n, edges))
    end = time.time()
    elapsed = end - start
    print(f'time elapsed: {elapsed}')