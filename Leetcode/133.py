class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):

        if node == None:
            return None
        
        queue = [(None,node)]
        visited = {}
        
        head = None

        while len(queue) != 0:
            visitParent = queue[0][0]
            visit = queue[0][1]

            if visit.label in visited:
                queue = queue[1:]
                continue
            else:
                visited[visit.label] = curr
                
            newParent = None

            curr = UndirectedGraphNode(visit.label)
            
            if head == None:
                head = curr
                
            if visitParent != None:
                if visitParent.label not in visited:
                    newParent = UndirectedGraphNode(visitParent.label)
                    newParent.neighbors.append(curr)
                elif visitParent.label in visited:
                    newParent = visited[visitParent.label]
                    newParent.neighbors.append(curr)
            
            for neighbor in visit.neighbors:
                queue.append((visit,neighbor))
                    
        #queue = [head]
        #visited = {}
        
        #while len(queue) != 0:
        #    visit = queue.pop()
        #    visited[visit] = True
        #    print(visit.label)
        #    for neighbor in visit.neighbors:
        #        if neighbor not in visited:
        #            queue.append(neighbor)

        return head
