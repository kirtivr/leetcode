from typing import List
import pdb
import sys

class Solution:
    def largestPermutation(self, nums_set: List[int]) -> bool:
        # is the set sorted in descending order?
        prev = None
        for idx, el in enumerate(nums_set):
            if prev is not None and prev < el:
                return False
            prev = el
        return True

    def nextPermutation(self, base_list: List[int]) -> List[int]:
        if (len(base_list) < 2):
            return base_list
        # pdb.set_trace()
        # Start from the last element, going to the front until we find an element that is
        # smaller than the largest element to its right.
        idx_to_change = None
        prev_largest_idx = len(base_list) - 1
        for i in range (prev_largest_idx, -1, -1):
            if base_list[i] < base_list[prev_largest_idx]:
                idx_to_change = i
                break
            else:
                prev_largest_idx = i

        # Now we need to find the index to the right of `idx_to_change` which is the
        # smallest element larger than base_list[idx_to_change].
        if idx_to_change == None:
            print("Something went wrong, this seems like it is sorted in descending order")
            return base_list

        smallest_larger_idx = prev_largest_idx
        for i in range(idx_to_change + 1, len(base_list), 1):
            if base_list[i] > base_list[idx_to_change] and base_list[i] < base_list[smallest_larger_idx]:
                smallest_larger_idx = i

        temp = base_list[smallest_larger_idx]
        base_list[smallest_larger_idx] = base_list[idx_to_change]
        base_list[idx_to_change] = temp
        
        # Sort remaining elements.
        sorted_subset = sorted(base_list[idx_to_change + 1:])
        result = base_list[:idx_to_change + 1] + sorted_subset
        return result
        
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums = [sorted(nums)]
        while (not self.largestPermutation(nums[-1])):
            nums.append(self.nextPermutation(nums[-1][:]))
            # print(nums)
        return nums
        
if __name__ == '__main__':
    x = Solution()
    nums = [1, 2, 3, 4]
    print(x.permuteUnique(nums))
