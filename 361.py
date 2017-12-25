class Solution(object):
    def dfs_search(self, grid, point):
        enemies = 0
        rows = len(grid[0])
        cols = len(grid)
        
        row_n = point[0]
        col_n = point[1]
        row = grid[row_n]
        col = [r[col_n] for r in grid ]
       
#        print(row)
#        print(col)
        
        #print(row_n)
#        print('col_n is ' + str(col_n))
        #print(cols)
        #print(rows)
    
        # row_search
        row_i = col_n + 1
        row_j = col_n - 1

        while row_i < rows:
            if row[row_i] == 'E':
                enemies = enemies + 1
            elif row[row_i] == 'W':
                break
            row_i = row_i + 1

        while row_j >= 0 and row_j < rows:
            if row[row_j] == 'E':
                enemies = enemies + 1
            elif row[row_j] == 'W':
                break
            row_j = row_j - 1

#        print('row enemies : '+str(enemies))
        # col_search
        col_i = row_n + 1
        col_j = row_n - 1

        while col_i < cols:

   #         print('col i '+str(col_i) + ' '+col[col_i])
            
            if col[col_i] == 'E':
                enemies = enemies + 1
            elif col[col_i] == 'W':
                break
            col_i = col_i + 1
    #    print('+col : '+str(enemies))
        
        while col_j >= 0 and col_j <cols:
            
 #           print('col j '+str(col_j) + ' '+col[col_j])

            if col[col_j] == 'E':
                enemies = enemies + 1
            elif col[col_j] == 'W':
                break
            col_j = col_j - 1

  #      print('col enemies : '+str(enemies))
        return enemies

    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        start_points = []
        grid_size = len(grid)
        
        for row in range(grid_size):
            for column in range(len(grid[row])):
                if grid[row][column] == '0':
                    start_points.append((row,column))

        max_killed = 0
        print (start_points)
        for pt in start_points:
            killed = self.dfs_search(grid, pt)
            if killed > max_killed:
                max_killed = killed

        return max_killed

if __name__ == '__main__':
    inp = ["0E00","E0WE","0E00"]
#    inp = ["000"]
#    inp = ["WWWWWWWWWW","EEEEEEEEEE","WWWWWWWWWW","0000000000","WWWWWWWWWW","EEEEEEEEEE"]
    for r in inp:
        print(r)
    print(Solution().maxKilledEnemies(inp))
