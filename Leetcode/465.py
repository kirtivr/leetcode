from typing import List, Optional, Tuple, Dict
from heapq import heappop, heappush, heapify
import pdb
import ast
import sys
from functools import cmp_to_key
import time

class Solution:
    def findCycleStartingFrom(self, connections: List[set[int]], vertex: int, visited: Dict[int, bool], path: List[int]) -> List[List[int]]:
        if vertex in visited:
            for i, v in enumerate(path):
                if v == vertex:
                    path.append(vertex)
                    print(f'cycle found ending at {vertex} path = {path}')
                    return [path[i:]]
            return []

        paths = []
        visited[vertex] = True
        path.append(vertex)
        # Add vertex to path, and explore its neighbors.
        canonical_path = len(path)
        for neighbor in connections[vertex]:
            path = path[:canonical_path]
            cycles = self.findCycleStartingFrom(connections, neighbor, visited, path)
            if len(cycles) > 0:
                for c in cycles:
                    paths.append(c)

        return paths

    def minTransfers(self, transactions: List[List[int]]) -> int:
        # Brute force approach:
        # Construct a graph from all transactions.
        #
        # For node A:
        #    If A -> B -> C -> A
        #    Check if debt can be simplified.
        #    Debt can be simplified if:
        #    A -> B + C -> A > B -> C.
        # Example:
        #    A owes B $10, B owes C $20, C owes A $10.
        #    B owes C $10.

        #    A owes B $10, B owes C $30, C owes A $10.
        #    B needs to pay C $10 ( B -> C - min(A -> B, C -> A))

        #    A owes B $5, B owes C $30, C owes A $15.
        #    B pays C $25. C pays A $10 ( C -> A - min(A -> B, B -> C)).


        # Find all cycles in the graph.
        # Find the minimum flow in the cycle, subtract it from all transactions and eliminate as many as possible.
        num_v = 0
        for t in transactions:
            num_v = max(t[0], t[1], num_v)

        num_v += 1
        connections = [set() for i in range(num_v)]
        weights = {}
        for edge in transactions:
            u = edge[0]
            v = edge[1]
            connections[u].add(v)
            weights[(u, v)] = edge[2]

        visited = {}
        print(f'weights = {weights}')
        for i in range(num_v):
            cycles = self.findCycleStartingFrom(connections, i, visited, [])
            print(f'cycles starting from {i} = {cycles}')
            for cycle in cycles:
                # A cycle is a collection of 2 or more nodes that are connected.
                N = len(cycle) - 1
                min_weight = float("inf")
                for i in range(N):
                    v1 = cycle[i]
                    v2 = cycle[i + 1]
                    min_weight = min(min_weight, weights[(v1, v2)])

                print(f'minimum weight for cycle {cycle} is {min_weight}')

                for i in range(N):
                    v1 = cycle[i]
                    v2 = cycle[i + 1]
                    # Adjust weights.
                    weight = weights[(v1, v2)] - min_weight
                    print(f'v1 = {v1} v2 = {v2} weights = {weights[(v1, v2)]} mw = {min_weight} weight = {weight}')
                    if weight == 0:
                        # Remove this connection.
                        del weights[(v1, v2)]
                        connections[v1].remove(v2)
                    else:
                        weights[(v1, v2)] = weight

        # All remaining connections are non-cyclic.
        debts = [0 for i in range(num_v)]
        for u in range(num_v):
            for v in connections[u]:
                debts[u] += weights[(u, v)]

        print(connections)
        print(weights)

        # Non cyclic case.
        # A -> B $30
        # B -> C $10
        # B -> D $10
        # B -> E $10
        def updateWeights(connections, taking_over, tof, weights):
            print(f'taking over = {taking_over} from = {tof} connections[from] = {connections[tof]}')
            for tofc in connections[tof]:
                if (taking_over, tofc) in weights:
                    weights[(taking_over, tofc)] += weights[(tof, tofc)]
                else:
                    weights[(taking_over, tofc)] = weights[(tof, tofc)]
                del weights[(tof, tofc)]

        def simplifyDebts(connections, u, v, weights, debts):
            if debts[v] <= weights[(u, v)]:
                connections[u].remove(v)
            # Adjusts debts, weights.
            weights[(u, v)] -= debts[v]
            debts[v] = 0
            # Update connections[u] and weights[u, (u, connection of v)]
            vc = connections[v]
            connections[u] = connections[u].union(vc)
            updateWeights(connections, u, v, weights)
            connections[v] = set()

        # A -> B can be eliminated, and A can pay C, D, E.
        for u in range(num_v):
            restart = True
            while restart:
                # u can pay off all of v's debts.
                #pdb.set_trace()
                restart = False
                ucc = set(connections[u])
                for v in ucc:
                    if debts[v] > 0 and debts[v] <= weights[(u, v)]:
                        simplifyDebts(connections, u, v, weights, debts)
                        restart = True

        #print(connections)
        print(weights)
        num_c = 0
        owed = set()
        for u in range(num_v):
            owed.add(v for v in connections[u])

        return num_c

if __name__ == '__main__':
    x = Solution()
    start = time.time()
    with open('465_tc.text', 'r') as f:
        #print(n)
        edges = ast.literal_eval(f.readline())
        #print(edges)
        print(x.minTransfers(edges))
    end = time.time()
    elapsed = end - start
    print(f'time elapsed: {elapsed}')