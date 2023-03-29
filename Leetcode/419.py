class Solution:
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        N = len(board)
        if N == 0:
            return 0
        M = len(board[0])
        count = 0
        
        for i in range(N):
            rowScanned = False
            for j in range(M):
                if board[i][j] == 'X':
                    if not rowScanned and (i == 0 or i > 0 and board[i-1][j] != 'X'):
                        #print('i == '+str(i) + ' j== '+str(j))
                        count += 1
                        rowScanned = True
                else:
                    rowScanned = False
        return count


if __name__ == '__main__':
    board = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]
    print(Solution().countBattleships(board))
