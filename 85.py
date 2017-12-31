class Solution:
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """

        table = {}

        rows = len(matrix)

        if rows == 0:
            return 0

        cols = len(matrix[0])

        for x in matrix:
            print(x)
            
        for i in range(rows):
            zeroIdx = None
            for j in range(cols):
                if matrix[i][j] == "1":
                    table[i,j] = []
                    if zeroIdx == None:
                        table[i,j].append(-1)
                    else:
                        table[i,j].append(zeroIdx)

                else:
                    zeroIdx = j

#        print(table)
            
        for i in range(cols):
            zeroIdx = None            
            for j in range(rows):
                if matrix[j][i] == "1":
                    if zeroIdx == None:
                        table[j,i].append(-1)
                    else:
                        table[j,i].append(zeroIdx)
                else:
                    zeroIdx = j        

        points = table.keys()

        largest = 1 if len(points) > 0 else 0
        
 #       print(points)
        for p1 in points:
            for p2 in points:
                if p1 != p2 and p1[0] <= p2[0] and p1[1] <= p2[1] and matrix[p2[0]][p1[1]] == "1" and matrix[p1[0]][p2[1]] == "1":
#                    print('++++ '+str(p1) + ' --- ' + str(p2) + ' +++')
                    c = [p1[0],p2[1]]
                    comp = p1[1]

                    while matrix[c[0]][c[1]] == "1":
                        if table[(c[0],c[1])][0] >= comp:
                            break
                        
                        if c[0] == p2[0]:
                            area = (p2[1]-p1[1]+1) * (p2[0]-p1[0]+1)
                            
                            if area > largest:
 #                               print('# '+ str(p1) + ' --- ' + str(p2)+' #')                           
                                largest = area
                                
                            break
                        print(c)
                        c[0] += 1
                        
        return largest


if __name__ == '__main__':
#    matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    matrix = [["1","0","1","1","0","1"],["1","1","1","1","1","1"],["0","1","1","0","1","1"],["1","1","1","0","1","0"],["0","1","1","1","1","1"],["1","1","0","1","1","1"]]
    print(Solution().maximalRectangle(matrix))
