class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        
        M = len(matrix)

        if M == 0:
            return matrix

        N = len(matrix[0])


        visited = {}

        def visit(row,col):
            nonlocal visited

            visited[(row,col)] = True

            rowsV = []
            colsV = []
            
            for c in range(N):
                if matrix[row][c] == 0 and (row,c) not in visited:
                    colsV.append(c)
                else:
                    visited[(row,c)] = True
                    
            for r in range(M):
                if matrix[r][col] == 0 and (r,col) not in visited:
                    rowsV.append(r)
                else:
                    visited[(r,col)] = True

            for r in rowsV:
                visit(r,col)

            for c in colsV:
                visit(row,c)


            # now color !

            for c in range(N):
                matrix[row][c] = 0
            for r in range(M):
                matrix[r][col] = 0

            return

        for i in range(M):
            for j in range(N):
                if matrix[i][j] == 0 and (i,j) not in visited:
                    visit(i,j)
                    
        

        print(matrix)
