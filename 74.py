class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        
        M = len(matrix)
        
        if M == 0 or len(matrix[0]) == 0:
            return False
        N = len(matrix[0])
        

        def searchCols(target,start,end):

            if start >= end:
                return -1

            mid = start + (end-start)//2
            print(mid)
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                return mid
            elif matrix[mid][0] > target:
                return searchCols(target,start,mid)
            else:
                return searchCols(target,mid+1,end)

        
        def searchRow(row,target,start,end):
            if start >= end:
                return False

            mid = start + (end-start)//2

            if row[mid] == target:
                return True
            elif row[mid] > target:
                return searchRow(row,target,start,mid)
            else:
                return searchRow(row,target,mid+1,end)

        col = searchCols(target,0,M)

        if col == -1:
            return False
        else:
            return searchRow(matrix[col],target,0,N)

            
if __name__ == '__main__':
    m = [
        [1,   3,  5,  7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ]
    t = 3
    m = [[1]]
    t = 0
    m = [[1],[3]]
    t = 3
    m = [[1]]
    t = 1
    m = [[1,3]]
    t = 3
    print(Solution().searchMatrix(m,t))
