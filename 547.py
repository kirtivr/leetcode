class Solution(object):
    def toVisit(self, v):
        for i in range in len(v):
            node = v[i]
            if node == False:
                return i
        return None

    def doVisit(self, rNum, M, visited):
        visited[rNum] = True
        for j in range(len(M)):
            if rNum != j and M[rNum][j] == 1 and not visited[j]:
                self.doVisit(j,M,visited)

    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """

        visited = [ False for j in range(len(M)) ]

        circles = 0

        numRows = len(M)

        for i in range(numRows):
            if visited[i]:
                continue
            
            self.doVisit(i,M,visited)
            circles = circles + 1
            
        return circles


if __name__ == '__main__':
    M = [[1,1,0],[1,1,0],[0,0,1]]

    print(Solution().findCircleNum(M))
