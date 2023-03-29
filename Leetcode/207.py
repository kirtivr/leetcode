class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        class Graph:
            def __init__(self,V):
                self.V = V
                self.edges = [[] for i in range(V)]

            def addEdge(self,source,dest):
                self.edges[dest].append(source)

            def topoSortUtil(self,source,visited,recStack):
                visited[source] = True
                recStack[source] = True

                for v in self.edges[source]:
                    if not visited[v]:
                        if self.topoSortUtil(v,visited,recStack):
                            return True
                    elif recStack[v]:
                        return True
                    
                recStack[source] = False
                return False
            
            def topoSort(self):
                s = [i for i in range(self.V)]
                visited = [False for i in range(self.V)]
                stk = [False for i in range(self.V)]
                
                for u in s:
                    if not visited[u]:
                        isCycle = self.topoSortUtil(u,visited,stk)
                        if isCycle:
                            return False
                return True
            
        g = Graph(numCourses)

        for pre in prerequisites:
            g.addEdge(pre[0],pre[1])

        if g.topoSort():
            return True
        else:
            return False


if __name__ == '__main__':
    N = 2
    ed = [[1,0],[0,1]]
    print(Solution().canFinish(N,ed))

        
