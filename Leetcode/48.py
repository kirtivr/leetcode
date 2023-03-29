class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """

        N = len(matrix)
        
        for i in range(N):
            for j in range(N//2):
                matrix[i][N-j-1],matrix[i][j] = matrix[i][j],matrix[i][N-j-1]

        #print(matrix)

        for i in range(N):
            for j in range(N-i-1):
                matrix[i][j], matrix[N-j-1][N-i-1]= matrix[N-j-1][N-i-1],matrix[i][j]
                
        return matrix
    
if __name__ == '__main__':

    matrix = [
        [ 5, 1, 9,11,3],
        [ 2, 4, 8,10,4],
        [13, 3, 6, 7,8],
        [15,14,12,16,14],
        [20,21,22,23,24]
    ]

    matrix = [
        [ 5, 1, 9,11],
        [ 2, 4, 8,10],
        [13, 3, 6, 7],
        [15,14,12,16]
    ]

    matrix = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
    print(Solution().rotate(matrix))
