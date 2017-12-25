class Solution(object):
    def tryBfs(self, nums, idx, visited):
        N = len(nums)

        if N == 0:
            return False
        
        queue = [idx]
        visited[idx] = True
        least = 0
        
        while len(queue) > 0:
            idx = queue.pop(0)
            currJump = nums[idx]
            
            for i in range(idx+currJump, least, -1):
                if i not in visited and i < N:
                    visited[i] = True
                    queue.append(i)
                    
            least = max(idx + currJump,least)
                    
        breadth = []
        for key in visited:
            breadth.append(key)
        
        return self.tryEasyJump(nums,breadth)

    def tryEasyJump(self, nums, breadth):
        N = len(nums)
        M = len(breadth)
        print(breadth)
        
        for i in range(M):
            jmp = nums[breadth[i]]
            if jmp + breadth[i] >= N-1:
                return True
        return False
    
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        visited = {}
        return self.tryBfs(nums,0,visited)

if __name__ == '__main__':
#    nums = [2,3,1,1,4]
    nums = [3,2,1,0,4]
    print(Solution().canJump(nums))
