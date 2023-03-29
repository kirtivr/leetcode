class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        rows = []
        minCol = float("inf")
        maxCol = -1

        M = len(matrix)
        if M == 0 or len(matrix[0]) == 0:
            return False
        N = len(matrix[0])

        def searchRows(target,start,end):
            nonlocal rows
            
            if start >= end:
                return
            
            mid = start + (end-start)//2

            if matrix[mid][0] <= target <= matrix[mid][-1]:
                rows.append(mid)
                searchRows(target,start,mid)
                searchRows(target,mid+1,end)
            elif matrix[mid][0] > target:
                searchRows(target,start,mid)
            else:
                searchRows(target,mid+1,end)

        def searchCols(target,start,end):
            nonlocal minCol,maxCol
            
            if start >= end:
                return
            
            mid = start + (end-start)//2

            if matrix[0][mid] <= target <= matrix[-1][mid]:
                minCol = min(mid,minCol)
                maxCol = max(mid,maxCol)
                searchCols(target,start,mid)
                searchCols(target,mid+1,end)
            elif matrix[0][mid] > target:
                searchCols(target,start,mid)
            else:
                searchCols(target,mid+1,end)

        def searchRow(row,target,start,end):
            if start >= end:
                return False
            mid = start + (end-start)//2
            print(row[mid])
            print(target)

            if row[mid] == target:
                return True
            elif row[mid] > target:
                return searchRow(row,target,start,mid)
            else:
                return searchRow(row,target,mid+1,end)

        searchRows(target,0,M)
        searchCols(target,0,N)

        for r in rows:
            row = m[r][minCol:maxCol+1]
            print(row)
            if searchRow(row,target,0,maxCol-minCol+1):
                return True
        return False
if __name__ == '__main__':
    m = [
        [1,   4,  7, 11, 15],
        [2,   5,  8, 12, 19],
        [3,   6,  9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]
    t = 5
    m = [[1]]
    t = 0
    #m = [[1],[3]]
    #t = 3
    #m = [[1]]
    #t = 1
  #  m = [[1,3]]
   # t = 3

    print(Solution().searchMatrix(m,t))

