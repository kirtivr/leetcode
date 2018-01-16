class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """

        parents = range(n)
        
        def findParent(self,a):
            if parents[a] == a:
                    return a
                else:
                    return findParent(parents[a])
                
        def union(self,a,b):
            if findParent(a) == findParent(b):
                return 0
            
            else:
                parents[findParent(a)] = parents[findParent(b)]
                return 1

        for e in edges:
            if union(e[0],e[1]) == 0:
                return False

        prev = None
        
        for p in parents:
            if prev == None:
                prev = findParent(p)
                continue
            else:
                if findParent(p) != prev:
                    return False
        return True
