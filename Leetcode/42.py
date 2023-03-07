from typing import List
import pdb

class Solution:
    def trap(self, height: List[int]) -> int:
        max_h = 0
        trapped = 0
        for h in range(0, len(height)):
            max_h = max(h, max_h)
        for sl in range(1, max_h):
            left = -1
            for idx in range(0, len(height)):
                if height[idx] >= sl and left == -1:
                    # start scanning from here
                    left = idx
                    continue
                if height[idx] >= sl and left != -1:
                    # some water may be trapped
                    distance = idx - left - 1
                    trapped += (distance)
                    #print('trapped '+ str(sl * distance) +' water' + ' between left = '+ str(left) + ' right = ' + str(idx))
                    left = idx
        return trapped

if __name__ == '__main__':
    #height = [0,1,0,2,1,0,1,3,2,1,2,1]
    height = [4,2,0,3,2,5]
    # adverse example: [2, 0, 2]
    x = Solution()
    print(x.trap(height))
