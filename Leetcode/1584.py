from typing import List, Optional, Tuple, Dict
import heapq
import pdb
import ast
import sys
from functools import cmp_to_key
import time
from dataclasses import dataclass, field
from typing import Any

@dataclass(order=True)
class PrioritizedItem:
    priority: int
    nodes: set[int]

    def __key(self):
        return self.nodes

    def __hash__(self):
        return hash(self.__key)

class Solution:
    '''def doBfsFrom(self, start: int) -> Dict[int, bool]:
        node_q = [start]
        visited = {}
        #print(f'starting from {start.name}')
        while node_q:
            v = node_q.pop(0)
            if v in visited:
                continue
            #print(f'visiting {v.name}')
            visited[v] = True
            for n_i in range(len(v.connections)):
                node_q.append(v.connections[n_i])
        return visited'''

    def mergeComponents(self, connected: List[Dict[int, bool]], node_B: int, connected_component_i: int) -> bool:
        for connected_component_j in range(len(connected)):
            if connected_component_i == connected_component_j:
                continue
            if node_B in connected[connected_component_j]:
                # We need to merge i and j, and remove component j.
                connected[connected_component_i].update(connected[connected_component_j])
                connected.pop(connected_component_j)
                return True

        # The other element is not in any component.
        connected[connected_component_i][node_B] = True
        return True

    def updateConnectedComponents(self, connected: List[Dict[int, bool]], node_A: int, node_B: int):
        for connected_component_i in range(len(connected)):
            # Connect related components together.
            if node_A in connected[connected_component_i]:
                self.mergeComponents(connected, node_B, connected_component_i)
                #print(connected)
                return
            # Now go the other way
            elif node_B in connected[connected_component_i]:
                self.mergeComponents(connected, node_A, connected_component_i)
                #print(connected)
                return
        connected.append({node_A: True, node_B: True})
        #print(connected)

    def treeCreated(self, connected: List[Dict[int, bool]], N: int) -> bool:
        return len(connected) == N

    def isConnected(self, connected: List[Dict[int, bool]], start: int, find: int) -> bool:
        for connected_component_i in range(len(connected)):
            if start in connected[connected_component_i] and find in connected[connected_component_i]:
                #print('in same component')
                return True
        return False

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        cost_matrix = {}
        pq = []
        ss = set()
        for i in range(len(points)):
            for j in range(len(points)):
                if i == j or (min(i, j), max(i, j)) in cost_matrix:
                    continue
                m_d = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                cost_matrix[(min(i, j), max(i, j))] = True

                item = PrioritizedItem(m_d, (min(i, j), max(i, j)))
                heapq.heappush(pq, item)
                ss.add(item)

        s = sorted(ss, key = lambda x: x.priority, reverse=True)
        #print(ss)
        total = 0
        connected_components = []
        #for edge in pq:
        #    print(f'{edge.nodes[0]} <-> {edge.nodes[1]} weight: {edge.priority}')
        while s:
            top = s.pop()
            #print(f'adding edge {top.nodes[0]} <-> {top.nodes[1]} weight: {top.priority}')
            node_A = top.nodes[0]
            node_B = top.nodes[1]
            if self.isConnected(connected_components, node_A, node_B):
                #print(f'{top.nodes[0]} is connected to {top.nodes[1]}')
                continue
            self.updateConnectedComponents(connected_components, node_A, node_B)
            total += top.priority
            if self.treeCreated(connected_components, N):
                return total
        return total

if __name__ == '__main__':
    x = Solution()
    start = time.time()
    with open('1584_tc.text', 'r') as f:
        points = ast.literal_eval(f.readline())
        print(x.minCostConnectPoints(points))
    end = time.time()
    elapsed = end - start
    print(f'time elapsed: {elapsed}')