class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        Ax = []

        row = 0
        for l in A:
            for i in range(len(l)):
                el = l[i]
                if el != 0:
                    Ax.append((row,i))
            row = row + 1
        
        Bx = []

        columns = 0 if (len(B) == 0 or len(B[0]) == 0) else len(B[0])

        m = len(A)
        n = columns
        
        C = [[0] * columns for i in range(m)]

        for i in range(columns):
            row = 0
            for l in B:
                el = l[i]
                if el != 0:
                    Bx.append((row,i))
                row = row + 1
                
        print(Ax)
        print(Bx)
        for row1,col1 in Ax:
            for row2,col2 in Bx:
                if col1 == row2:
                    C[row1][col2] = C[row1][col2] + A[row1][col1] * B[row2][col2]

        return C


if __name__ == '__main__':
    #A = [
    #    [ 1, 0, 0],
    #    [-1, 0, 3]
    #]
    
    #B = [
    #    [ 7, 0, 0 ],
    #    [ 0, 0, 0 ],
    #    [ 0, 0, 1 ]
    #]

    A = [[1,-5]]
    B = [[12],[-1]]

    print(Solution().multiply(A,B))
                
                
