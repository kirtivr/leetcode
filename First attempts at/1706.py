#!/usr/bin/env python
import time
import pdb
import sys
import copy
from typing import List, TypedDict, Tuple

class Solution:
    def generateActions(self, grid: List[List[int]], actions: List[List[int]]):
        # 0 stands for stop. 1 stands for bottom right. 2 stands for bottom left.
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                # Cover the case where the ball gets sent beyond the wall.
                if col == 0 and grid[row][col] == -1:
                    actions[row][col] = 0
                if col == len(grid[row]) - 1 and row != len(grid) - 1 and grid[row][col] == 1:
                    actions[row][col] = 0

                # We have two cases:
                # 1. Slide to the bottom left
                #    Occurs when [row][col] and [row][col - 1] are both -1.
                # 2. Slide to the bottom right
                #    Occurs when [row][col] and [row][col + 1] are both 1.
                if grid[row][col] == 1 and col != len(grid[row]) - 1 and grid[row][col + 1] == 1:
                    actions[row][col] = 1
                if grid[row][col] == -1 and col > 0 and grid[row][col - 1] == -1:
                    actions[row][col] = 2
#                if col == len(grid[row]) - 1 and row == len(grid) - 1 and grid[row][col] == 1:
#                    actions[row][col] = 1
#                if col == 0 and row == len(grid) - 1 and grid[row][col] == -1:
#                    actions[row][col] = 2

        return actions

    def simulateStartingFrom(self, start: Tuple[int, int], grid: List[List[int]], actions: List[List[int]]) -> int:
        (row, col) = start
#        print(f'start = {(row, col)}')
        while row <= len(grid) - 1 and col <= len(grid[0]) - 1 and actions[row][col] != 0:
            # Go bottom right
            if actions[row][col] == 1:
#                print('go bottom right')
                col += 1
            elif actions[row][col] == 2:
#                print('go bottom left')
                col -= 1
            row += 1
#            print(f'next = {(row, col)}')
        if row == len(grid):
            return col

        return -1

    def findBall(self, grid: List[List[int]]) -> List[int]:
        actions = [[0 for i in range(len(grid[j]))] for j in range(len(grid))]
        self.generateActions(grid, actions)
        print(actions)
        out = []
        for i in range(len(grid[0])):
            out.append(self.simulateStartingFrom((0, i), grid, actions))

        return out
        
if __name__ == '__main__':
    x = Solution()
    start = time.time()
#    grid = [[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]
    grid = [[-1]]
#    grid = [[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1],[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1]]
    print(x.findBall(grid))
    end = time.time()
    elapsed = end - start
    print (f'time elapsed = {elapsed}')
