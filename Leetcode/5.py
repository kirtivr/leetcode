class Solution(object):
    def checkForEvenPalin(self, subs, midIdx, maxLen):
        leftIdx = midIdx
        rightIdx = midIdx + 1

        maxPalin = 0
        
        while leftIdx >= 0 and rightIdx < maxLen:
            if subs[leftIdx] == subs[rightIdx]:
                maxPalin = rightIdx - leftIdx + 1
                leftIdx = leftIdx - 1
                rightIdx = rightIdx + 1
            else:
                break

        leftIdx = max(leftIdx+1, 0)
        rightIdx = min(rightIdx, maxLen)

        return (maxPalin, subs[leftIdx:rightIdx])
    
    def checkForOddPalin(self, subs, midIdx, maxLen):
        leftIdx = midIdx - 1
        rightIdx = midIdx + 1

        maxPalin = 0
        
        while leftIdx >= 0 and rightIdx < maxLen:
            if subs[leftIdx] == subs[rightIdx]:
                maxPalin = rightIdx - leftIdx + 1
                leftIdx = leftIdx - 1
                rightIdx = rightIdx + 1
            else:
                break

        leftIdx = max(leftIdx+1, 0)
        rightIdx = min(rightIdx, maxLen)

        return (maxPalin, subs[leftIdx:rightIdx])
    
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        sLen = len(s)
        if sLen == 0:
            return ""
        
        maxPalin = 0
        palinString = s[0]
        
        for idx, ch in enumerate(s):
            (evenPLen, evenS) = self.checkForEvenPalin(s, idx, sLen)
            (oddPLen,oddS) = self.checkForOddPalin(s, idx, sLen)

            #print('even '+evenS)
            #print('odd '+oddS)
            
            if maxPalin < evenPLen:
                maxPalin = evenPLen
                palinString = evenS

            elif maxPalin < oddPLen:
                maxPalin = oddPLen
                palinString = oddS
                
        return palinString
