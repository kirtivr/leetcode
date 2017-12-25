class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """


        rows = len(board)

        if rows == 0 or word == "":
            return False
        
        cols = len(board[0])


        def look(pt, remaining):
            #print(remaining)
            #print(' pt '+str(pt[0])+','+str(pt[1]))
            #for row in visited:
             #   print(row)
            
            if len(remaining) == 0:
                return True
            
            if board[pt[0]][pt[1]] != remaining[0]:
                return False
            
            temp = board[pt[0]][pt[1]]
            board[pt[0]][pt[1]] = '#'
            
            remaining = remaining[1:]

            top = pt[0] - 1
            bot = pt[0] + 1
            right = pt[1] + 1
            left = pt[1] - 1

            
            if top >= 0 and look((top,pt[1]), remaining):
                    return True
                    
            if bot < rows and look((bot,pt[1]), remaining):
                    return True

            if left >= 0 and look((pt[0],left), remaining):
                    return True

            if right < cols and look((pt[0],right), remaining):
                    return True
            
            board[pt[0]][pt[1]] = temp
            
            return False if len(remaining) > 0 else True
        
        #print(start) 
        for i in range(rows):
            for j in range(cols):
                if look((i,j), word):
                    return True

        return False

if __name__ == '__main__':
    s = [
        ['A','B','C','E'],
        ['S','F','C','S'],
        ['A','D','E','E']
    ]

    s = [["a"]]
    word = "ABCCED"
    word = "a"
    s = [["a","b"]]
    word = "ba"
    s = [["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]]
    word = "ABCESEEEFS"
    s = 
    print(Solution().exist(s,word))
