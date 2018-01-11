class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        undash = ''
        for char in S:
            if char != '-':
                undash = undash + char

        length = len(undash)
        
        groups = int(length / K)
        firstPart = length % K
        
        allStrings = []

        if firstPart:
            allStrings.append(undash[:firstPart])
        
        for i in range(groups):
            allStrings.append(undash[firstPart + K*i : firstPart + K*(i+1)])


        buildStr = ''
        if allStrings:
            buildStr = allStrings[0]
        
        for i in range(1,len(allStrings)):
            buildStr = buildStr + '-' + allStrings[i]

        return buildStr.upper()
