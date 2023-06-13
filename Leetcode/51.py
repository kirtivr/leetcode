from typing import List, Optional, Tuple, Dict
from heapq import heappop, heappush, heapify
import pdb
import ast
import sys
from functools import cmp_to_key
import time

class Solution:
    def boardToHashableString(self, board):
        #print(board)
        return ''.join(''.join(board[row_idx]) for row_idx in range(len(board)))

    def boardToString(self, board):
        #print(board)
        out = []
        for row in board:
            out.append(''.join(row))
        return out
    
    def boardIsValid(self, board):
        # This can be made more efficient by using a dictionary for all active queens
        # enumerating and sorting the keys, instead of using O(n^2) search.

        # No two queens in same row.
        for row in board:
            q = False
            for box in row:
                if box == 'Q':
                    if q:
                        return False
                    else:
                        q = True

        # No two queens in same column.
        for col in range(len(board)):
            q = False
            for row in range(len(board[0])):
                if board[row][col] == 'Q':
                    if q:
                        return False
                    else:
                        q = True
        
        def diagonalFromPointIsValid(board, point, n):
            # First go up and left.
            rowm = -1
            colm = -1
                        
            def testDiagonalWithModifiers(board, point, n, rowm, colm):
                current_row = point[0] + rowm
                current_col = point[1] + colm
                while current_row >= 0 and current_row < n and current_col >= 0 and current_col < n:
                    if board[current_row][current_col] == 'Q':
                        return False
                    current_row += rowm
                    current_col += colm
                return True

            if not testDiagonalWithModifiers(board, point, n, rowm, colm):
                return False
            
            # Up and right.
            rowm = -1
            colm = 1
            if not testDiagonalWithModifiers(board, point, n, rowm, colm):
                return False

            # Down and left.
            rowm = 1
            colm = -1
            if not testDiagonalWithModifiers(board, point, n, rowm, colm):
                return False

            # Down and right.
            rowm = 1
            colm = 1
            if not testDiagonalWithModifiers(board, point, n, rowm, colm):
                return False

            return True            

        # No two queens in same diagonal.
        for col in range(len(board)):
            for row in range(len(board[0])):
                if board[row][col] == 'Q' and not diagonalFromPointIsValid(board, (row, col), len(board)):
                    return False
        
        return True
        
    def solveBoard(self, current_row, board, visited, result):
        if current_row == len(board):
            # We have a valid placement of queens.
            result.append(self.boardToString(board))
            return
        
        board_hash = self.boardToHashableString(board)
        if (board_hash in visited):
            return visited[board_hash]
        
        for col_idx in range(len(board[current_row])):
            # Place a queen at col_idx.
            board[current_row][col_idx] = 'Q'
            if self.boardIsValid(board):
                worked = self.solveBoard(current_row + 1, board, visited, result)
                if worked:
                    visited[self.boardToHashableString(board)] = True
                else:
                    visited[self.boardToHashableString(board)] = False
            board[current_row][col_idx] = '.'

    def solveNQueens(self, n: int) -> List[List[str]]:
        # Approach, create a state of the chessboard, and use
        # backtracking to place the queen at some starting position or the
        # other. Use memoization to ensure we save stored board states.
        result = []        
        empty_board = [['.' for i in range(n)] for j in range(n)]
        visited = {}
        
        self.solveBoard(0, empty_board, visited, result)
        return result

if __name__ == '__main__':
    x = Solution()
    start = time.time()
    n = 9
    #print(edges)
    print(x.solveNQueens(n))
    end = time.time()
    elapsed = end - start
    print(f'time elapsed: {elapsed}')