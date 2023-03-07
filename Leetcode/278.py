from typing import List

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def isBadVersion(self, n: int) -> bool:
        if n < 4:
            return False
        return True

    def firstBadVersion(self, n: int) -> int:
      def binary_search(start: int, end: int) -> int:
        if start > end:
          return -1

        mid = start + (end - start)//2
        if self.isBadVersion(mid) and (mid == 0 or not self.isBadVersion(mid - 1)):
          print(f'mid eq = %d', mid)
          return mid
        elif not self.isBadVersion(mid):
          print(f'mid lt = %d end = %d', mid, end)
          return binary_search(mid+1, end)
        else:
          print(f'mid gt = %d', mid)
          return binary_search(start, mid-1)

      binary_search(0, N-1)

if __name__ == '__main__':
    N = 5
    x = Solution()
    x.firstBadVersion(N)
