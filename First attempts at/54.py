#!/usr/bin/env python
import time
import pdb
import sys
import copy
from typing import List, Tuple, TypedDict

class Solution:
    def doSpiral(self, matrix: List[List[int]], origin: Tuple[int, int], points: List[int],
                 visited: List[List[int]]) -> List[int]:
        o_row = origin[0]
        o_col = origin[1]
        f_row = len(matrix) - o_row - 1
        f_col = len(matrix[0]) - o_col - 1

        row = o_row
        col = o_col
        for col in range(o_col, f_col + 1, 1):
#            print(f'go right row = {row} col = {col}')
            if visited[row][col]:
                return True
            visited[row][col] = True
            points.append(matrix[row][col])

        for row in range(o_row + 1, f_row + 1, 1):
 #           print(f'go down row = {row} col = {col}')
            if visited[row][col]:
                return True
            visited[row][col] = True
            points.append(matrix[row][col])

        for col in range(col - 1, o_col - 1, -1):
 #           print(f'go left row = {row} col = {col}')
            if visited[row][col]:
                return True
            visited[row][col] = True
            points.append(matrix[row][col])

        for row in range(row - 1, o_row, -1):
 #           print(f'go up row = {row} col = {col}')
            if visited[row][col]:
                return True
            visited[row][col] = True
            points.append(matrix[row][col])

        return False

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        visited = [[False for i in range(len(matrix[j]))] for j in range(len(matrix))]
        origin = (0, 0)
        points = []
        o_p_len = len(points)
        while not self.doSpiral(matrix, origin, points, visited):
            if len(points) == o_p_len:
                break
            else:
                o_p_len = len(points)
            origin = (origin[0] + 1, origin[1] + 1)
#            pdb.set_trace()

        return points

if __name__ == '__main__':
    x = Solution()
    start = time.time()
#    grid = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    grid = [[1,2,3],[4,5,6],[7,8,9]]
    print(x.spiralOrder(grid))
    end = time.time()
    elapsed = end - start
    print (f'time elapsed = {elapsed}')
