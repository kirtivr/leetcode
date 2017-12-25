class Solution(object):
    def __init__(self):
        self.mappings = [[' '],['*'],['abc'],['def'],['ghi'],['jkl'],['mno'],['pqrs'],['tuv'],['wxyz']]

    def backTrack(self, cStr, digits):
 #       print(cStr)
        if len(digits) == 0:
#            print(cStr)
            return [cStr]
        
        digit = digits[0]
        n = ord(digit) - ord("0")
        letters = self.mappings[n][0]
        digits = digits[1:]

        allStrs = []
        
        for letter in letters:
            pStr = cStr + str(letter)
            newStrs = self.backTrack(pStr, digits)
            allStrs.extend(newStrs)
            
        return allStrs
        
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        allStrs = self.backTrack('',digits)

        return allStrs

if __name__ == '__main__':
    print(Solution().letterCombinations("23"))
