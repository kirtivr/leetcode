class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        table = {}

        for x in nums:
            table[x] = table.get(x,0) + 1
        
        #print(table)

        bucket = [[] for i in range(len(nums))]
        #print(bucket)
        
        for key,value in table.items():
            bucket[value-1].append(key)
#        print(bucket)

        out = []
        lim = k
        
        for i in range(len(nums)-1,-1,-1):
            if bucket[i]:
                if lim > 0:
                    for j in range(len(bucket[i])):
                        out.append(bucket[i][j])
                        lim -= 1
                        if lim == 0:
                            break
                else:
                    break
                            
        return out
