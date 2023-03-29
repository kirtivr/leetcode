class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        
        m = len(obstacleGrid)
        n = len(obstacleGrid[0]) if m >=1 else 0

        count = [[0 for i in range(n)] for j in range(m)]
        
        if m == 1 and n == 1:
            return 0 if obstacleGrid[0][0] == 1 else 1

        if m == 1:
            for i in range(0,n):
                if obstacleGrid[0][i] == 1:
                    return 0
            return 1
        
        elif  n == 1:
            for i in range(0,m):
                if obstacleGrid[i][0] == 1:
                    return 0
            return 1
        elif obstacleGrid[m-1][n-1] == 1:
            return 0
        
        for i in range(0,m):
            for j in range(0,n):
                if obstacleGrid[i][j] == 1 or (j == 0 and i>0 and count[i-1][j] == 0) or (i == 0 and j>0 and count[i][j-1] == 0):
                    count[i][j] = 0
                elif i == 0 or j == 0:
                    count[i][j] = 1
                else:
                    count[i][j] = count[i-1][j] + count[i][j-1]

        print(count)
        
        return count[m-1][n-1]

if __name__ == '__main__':
    grid = [[0, 0]]
#    grid = [[0,1,0,0,0],[1,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
    #grid = [[0,0],[1,1],[0,0]]
    #grid = [[0,0],[1,0]]
    print(Solution().uniquePathsWithObstacles(grid))
