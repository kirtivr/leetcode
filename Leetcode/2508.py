from typing import List, Optional, Tuple, Dict
import pdb
import ast
from functools import cmp_to_key
import time
import sys

class Solution:
    def solveGraph(self, can_connect: Dict[int, List[int]], oddVertices: Dict[int, bool], used: int):
    #, connections_made: List[Tuple[int, int]]):
        if len(oddVertices) == 0:
            #print(connections_made)
            return True

        if len(oddVertices) > 4:
            return False

        if used >= 2:
            return False

        oddVerticesList = list(oddVertices.keys())
        for vertex in oddVerticesList:
#            pdb.set_trace()
            # Make changes to propagate to the subproblem.
            del oddVertices[vertex]
            connections = list(can_connect[vertex])
            for connection in connections:
                #print(f'vertex = {vertex} connection = {connection} oddVertices = {oddVertices}')
#                pdb.set_trace()
                # We cannot connect between vertex and connection again.
                can_connect[vertex].remove(connection)
                if vertex in can_connect[connection]:
                    can_connect[connection].remove(vertex)
                #connections_made.append((vertex, connection))
                odd_connection = False
                if connection in oddVertices:
                    # Connection has now become even.
                    del oddVertices[connection]
                    odd_connection = True
                else:
                    # Connection has now become odd.
                    oddVertices[connection] = True
                if self.solveGraph(can_connect, oddVertices, used + 1):#, connections_made):
                    return True
                if odd_connection:
                    oddVertices[connection] = True
                else:
                    # Connection had become odd.
                    del oddVertices[connection]
                can_connect[vertex].append(connection)
                can_connect[connection].append(vertex)
                #connections_made.pop()
            # Vertex is odd and cannot connect to any other vertex.
            oddVertices[vertex] = True
        return False

    def buildConnectionGraph(self, connections: Dict[int, List[int]], oddVertices: List[int], n: int):
        if not oddVertices:
            return ({}, oddVertices)

        cq = list(oddVertices)
        can_connect = {i:[] for i in range(1, n + 1)}
        all_connections = set(i for i in range(1, n + 1))
        def isOdd(elem):
            return elem in oddVertices
        while cq:
            vertex = cq.pop()
            actual_connections = set(connections[vertex]) if vertex in connections else set()
            can_connect[vertex] = sorted([v for v in all_connections.difference(actual_connections)], key = isOdd, reverse=True)

        return (can_connect, oddVertices)

    def findUnconnectedVertices(self, n: int, edges: List[List[int]]) -> Dict[int, List[int]]:
        connections = {}
        actual_connections = {}
        for edge in edges:
            if edge[0] not in actual_connections:
                actual_connections[edge[0]] = [edge[1]]
            else:
                actual_connections[edge[0]].append(edge[1])
            if edge[1] not in actual_connections:
                actual_connections[edge[1]] = [edge[0]]
            else:
                actual_connections[edge[1]].append(edge[0])
        
        oddVertices = {}
        # Find all odd vertices and build a connection graph from there.
        for source, vl in actual_connections.items():
            if len(vl) % 2 != 0:
                oddVertices[source] = True

        return self.buildConnectionGraph(actual_connections, oddVertices, n)
        
    def isPossible(self, n: int, edges: List[List[int]]) -> bool:
        (connections, oddVertices) = self.findUnconnectedVertices(n, edges)
        #print('-------\n' + str(oddVertices))
        #print('------\n' + str(connections))
        return self.solveGraph(connections, oddVertices, 0)#, [])

if __name__ == '__main__':
    x = Solution()
    start = time.time()
    n = 4
    #edges = [[1,2],[1,3],[1,4]]
    edges = [[1,2],[3,4]]
    #n = 5
    #edges = [[1,2],[2,3],[3,4],[4,2],[1,4],[2,5]]
    n = 11
    edges = [[5,9],[8,1],[2,3],[7,10],[3,6],[6,7],[7,8],[5,1],[5,7],[10,11],[3,7],[6,11],[8,11],[3,4],[8,9],[9,1],[2,10],[9,11],[5,11],[2,5],[8,10],[2,7],[4,1],[3,10],[6,1],[4,9],[4,6],[4,5],[2,4],[2,11],[5,8],[6,9],[4,10],[3,11],[4,7],[3,5],[7,1],[2,9],[6,10],[10,1],[5,6],[3,9],[2,6],[7,9],[4,11],[4,8],[6,8],[3,8],[9,10],[5,10],[2,8],[7,11]]
    n = 16
    edges = [[3,14],[14,10],[10,15],[16,11],[11,7],[4,8],[15,12],[12,9],[1,10],[14,7],[8,5],[9,3],[15,11],[10,12],[15,6],[16,13],[2,13],[2,8],[13,1],[6,11],[7,15],[7,10],[13,12],[16,9],[10,2],[14,13],[13,3],[7,12],[14,16],[12,14],[11,8],[9,13],[15,16],[8,14],[3,4],[11,9],[1,16],[9,15],[13,15],[5,7],[12,5],[16,2],[5,14],[12,1]]
    print(x.isPossible(n, edges))
    with open('test_case.text', 'r') as f:
        n = ast.literal_eval(f.readline())
        #print(n)
        edges = ast.literal_eval(f.readline())
        #print(edges)
        print(x.isPossible(n, edges))
    end = time.time()
    elapsed = end - start
    print(f'time elapsed: {elapsed}')