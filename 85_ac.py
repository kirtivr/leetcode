class Solution:
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """

        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0

        for x in matrix:
            print(x)

        rows = len(matrix)
        cols = len(matrix[0])

        rect = 0
        h = [0 for i in range(cols+1)]
        stk = []
        for i in range(rows):
            stk = []

            for j in range(cols+1):
                if j < cols:
                    if matrix[i][j] == '1':
                        h[j] += 1
                    else:
                        h[j] = 0
                        
                while len(stk) > 0 and h[j] < h[stk[-1]]:
                    print('i = '+str(i)+' h['+str(j)+'] = '+str(h[j])+ ' h['+str(stk[-1])+'] = ' +str(h[stk[-1]]))
                    top = stk.pop()
                    area = h[top] * (j - stk[-1] - 1 if len(stk) > 0 else j)
                    rect = max(area,rect)
                    
                    print('area = '+str(area)+' rect = ' +str(rect))
                stk.append(j)
                
        return rect

if __name__ == '__main__':
#    matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
#    matrix = [["1","0","1","1","0","1"],["1","1","1","1","1","1"],["0","1","1","0","1","1"],["1","1","1","0","1","0"],["0","1","1","1","1","1"],["1","1","0","1","1","1"]]
    matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    print(Solution().maximalRectangle(matrix))
