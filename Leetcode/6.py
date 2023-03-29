class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s

        L = [''] * numRows
        index, step = 0, 1

        for x in s:
            L[index] = L[index] + x
            if index == 0:
                step - 1
            elif index == numRows - 1:
                step = -1
            index = index + step

        return ''.join(L)
    
if __name__ == '__main__':
#    s = "PAYPALISHIRING"
#    n = 3
    #s = "A"
    #n = 1
    s = "ABCD"
    n = 3
#    s = "ABC"
#    n = 2
    s = "ABCDE"
    n = 4

    s = "ABCDE"
    n = 5
    print(Solution().convert(s,n))
