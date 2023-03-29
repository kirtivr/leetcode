class Solution(object):

    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        grid_size = len(grid)
        grid_row_sz = len(grid[0]) if grid_size > 0 else 0
        max_killed = 0
        rowhits = 0
        colhits = []

        for j in range(grid_row_sz):
            colhits.append(0)

        for i in range(grid_size):
            for j in range(grid_row_sz):
    
                if( j == 0 or grid[i][j-1] == 'W'):
                    rowhits = 0

                    for k in range(j,grid_row_sz):
                        if grid[i][k] == 'W':
                            break
                        rowhits = rowhits + ( 1 if grid[i][k] == 'E' else 0)

                if( i == 0 or grid[i-1][j] == 'W'):
                    colhits[j] = 0

                    for k in range(i,grid_size):
                        if grid[k][j] == 'W':
                            break
                        colhits[j] = colhits[j] + ( 1 if grid[k][j] == 'E' else 0)

                if (grid[i][j] == '0'):
                    max_killed = max(max_killed, rowhits + colhits[j])

        return max_killed

if __name__ == '__main__':
    inp = ["0E00","E0WE","0E00"]
#    inp = ["000"]
#    inp = ["WWWWWWWWWW","EEEEEEEEEE","WWWWWWWWWW","0000000000","WWWWWWWWWW","EEEEEEEEEE"]
    for r in inp:
        print(r)
    print(Solution().maxKilledEnemies(inp))
