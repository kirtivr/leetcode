class Solution(object):
    def doDfs(self, x, y, grid, visited, m, n):

        if x > m-1 or y > n-1 or x < 0 or y < 0 or grid[x][y] == "0" :
            return visited
        
 #       print("visited "+str(x)+" , "+str(y))
        visited[(x,y)] = True

        if (x-1,y) not in visited:
            visited = self.doDfs(x-1,y,grid,visited,m,n)

        if (x+1,y) not in visited:
            visited = self.doDfs(x+1,y,grid,visited,m,n)

        if (x,y+1) not in visited:
            visited = self.doDfs(x,y+1,grid,visited,m,n)

        if (x,y-1) not in visited:
            visited = self.doDfs(x,y-1,grid,visited,m,n) 

        return visited
    
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m = len(grid)

        if m == 0:
            return 0

        n = len(grid[0])

        visited = {}

        nIslands = 0
        
        for i in range(m):
            for j in range(n):
                if (i,j) not in visited and grid[i][j] == "1":
                    visited = self.doDfs(i, j, grid, visited, m, n)
                    nIslands = nIslands + 1
#                    print('--')
        return nIslands

        

if __name__ == '__main__':
#    grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
    grid = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
    for row in grid:
        print(row)
    print(Solution().numIslands(grid))
