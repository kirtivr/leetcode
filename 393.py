class Solution(object):
    def convertToBase2Str(self, num):
        binaryStr = ''

        while num > 0:
            if num%2 == 1:
                binaryStr = '1' + binaryStr
            else:
                binaryStr = '0' + binaryStr
            num = int(num / 2)

        zeroPrepend = 8 - len(binaryStr)
        for i in range(zeroPrepend):
            binaryStr = '0' + binaryStr

        return binaryStr

    def countLeadingOnes(self,binstr):
        for i in range(len(binstr)):
            if binstr[i] == '0':
                break
        
        return i
        
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """

        index = 0

        while index < len(data):
            
            binstr = self.convertToBase2Str(data[index])
            print(binstr)
            ones = self.countLeadingOnes(binstr)
            print(ones)

            if ones > len(data[index:]) or ones > 4:
                return False
            
            if ones == 0:
                index = index + 1
                continue
            elif binstr[:2] == '10':
                return False
            elif len(data[index:]) == 1 and ones != 0:
                return False
            
            i = 1
            index = index + 1
            
            while i < ones and index < len(data):
                binstr = self.convertToBase2Str(data[index])
                if binstr[:2] != '10':
                    return False
                
                index = index + 1
                i = i + 1

        return True

if __name__ == '__main__':
#    inp = [240, 162, 138, 147]
    inp = [197, 130, 1]
#    inp = [145]
    print(Solution().validUtf8(inp))

