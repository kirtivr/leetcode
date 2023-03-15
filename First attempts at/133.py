from typing import TypedDict

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Visited(TypedDict):
    key: int
    val: Node

class Solution:
    def dfsAndCopy(self, node: Node, visited: Visited) -> Node:
        # Do a depth first traversal of the input graph, creating the clone graph along the way.
        if node == None:
            return node
        if node.val in visited:
            return visited[node.val]

        clone_node = Node()
        clone_node.val = node.val
        visited[node.val] = clone_node
        
        for neighbor in node.neighbors:
            #print(f'{node.val}"s neighbor is {neighbor.val}')
            if neighbor.val in visited:
                clone_node.neighbors.append(visited[neighbor.val])
                continue

            clone_node.neighbors.append(self.dfsAndCopy(neighbor, visited))

        return clone_node

    def cloneGraph(self, node: Node) -> Node:
        visited = Visited()
        return self.dfsAndCopy(node, visited)

if __name__ == '__main__':
#    nodes_list = [[2,4],[1,3],[2,4],[1,3]]
    one = Node()
    one.val = 1
    two = Node()
    two.val = 2
    three = Node()
    three.val = 3
    four = Node()
    four.val = 4
    four.neighbors = [one, three]
    three.neighbors = [two, four]
    two.neighbors = [one, three]
    one.neighbors = [two, four]

    x = Solution()
    cloned = x.cloneGraph(one)
    print(f'is one == cloned ? {one == cloned}')
    cloned2 = x.cloneGraph(cloned)
