class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        maxLength = 0

        table = {0:0}

        for (index,num) in enumerate(nums):
            if num == 0:
                count -= 1
            else:
                count += 1

            if count in table:
                maxLength = max(maxLength, index - table[count])
            else:
                table[count] = index
        print(table)
        return maxLength
    
if __name__ == '__main__':
    inp = [1,1,1,1,1,1,1,0,0,0,0,1,1,0,1,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0,1,0,0,0,0,1,0,1,0,0,0,1,1,0,0,0,0,1,0,0,1,1,1,1,1,0,0,1,0,1,1,0,0,0,1,0,0,0,1,1,1,0,1,1,0,1,0,0,1,1,0,1,0,0,1,1,1,0,0,1,0,1,1,1,0,0,1,0,1,1]
#    inp = [0,1]
    #inp = [0,1,1,0,1,1,1,0]
    print(Solution().findMaxLength(inp))

