class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        rev = s[::-1]
        N = len(rev)

        num = 0
        mapping = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}

        prev = None
        
        for i in range(N):
            curr = rev[i]
            if i == 0:
                prev = curr
                num = mapping[curr]
            else:
                if mapping[curr] >= mapping[prev]:
                    prev = curr
                    num += mapping[curr]
                else:
                    prev = curr
                    num -= mapping[curr]
        return num
