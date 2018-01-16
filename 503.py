class Solution:
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        out = []
        els = {}
        
        N = len(nums)
        for i in range(N):
            out.append(-1)
            els[nums[i]] = -1
            
        stk = []
        for i in range(len(nums)*2):
            x = nums[i%N]
            #print(stk)
            
            if len(stk) == 0:
                stk.append((x,i%N))
            else:
                (top,idx) = stk[-1]
                
                while x > top and len(stk) > 0:
                    if els[top] == -1:
                        out[idx] = x
                    stk.pop()
                    if len(stk) > 0:
                        (top,idx) = stk[-1]
                    
                stk.append((x,i%N))


        #print(els)
        return out


if __name__ == '__main__':
    nums1 = [1,2,1]
    print(Solution().nextGreaterElements(nums1))
