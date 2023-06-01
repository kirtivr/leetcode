from typing import List
import pdb

class Solution:
    def calculateTrappedWater(self, left: int, right: int, heights: List[int], trapped: List[int]):
        for idx in range(right - 1, left, -1):
            effective_height_at_idx = heights[idx] + trapped[idx]
            water_line = min(heights[left], heights[right])
            if water_line > effective_height_at_idx:
                trapped[idx] = water_line - heights[idx]
            else:
                return
        return
            
    def trap(self, heights: List[int]) -> int:
        # Go from left to right, keeping track of the largest left wall.
        # For a new index, figure out if water was trapped for index - 1 to left.
        largest_left_idx = 0
        # Keep track of water that is already trapped.
        trapped = [0 for i in range(len(heights))]
        for right, wall in enumerate(heights):
            if right == 0:
                continue
            self.calculateTrappedWater(largest_left_idx, right, heights, trapped)
            if wall >= heights[largest_left_idx]:
                largest_left_idx = right
        total_trapped = 0
        for _, trapped_water in enumerate(trapped):
            #print(f'trapped at idx {_}: {trapped_water}')
            total_trapped += trapped_water
        return total_trapped

if __name__ == '__main__':
    heights = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    #heights = [2, 0, 2]
    #heights = [4, 2, 3]
    x = Solution()
    print(x.trap(heights))