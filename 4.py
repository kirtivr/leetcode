class Solution(object):

    def median(self, A, B):
        m, n = len(A), len(B)
        if m > n:
            A, B, m, n = B, A, n, m
        if n == 0:
            raise ValueError

        # A is lesser than eq B in size
        
        imin, imax, half_len = 0, m, (m + n + 1) // 2

        # imin, imax track the dimenstions of smaller array
    
        while imin <= imax:
            i = (imin + imax) // 2
            # i stores mid point of smaller array
            j = half_len - i
            # j is the difference of median point in combined array and current value of i
            
            if i < m and B[j-1] > A[i]:
                # i is too small, must increase it
                imin = i + 1
            elif i > 0 and A[i-1] > B[j]:
                # i is too big, must decrease it
                imax = i - 1
            else:
                # i is perfect

                if i == 0: max_of_left = B[j-1]
                elif j == 0: max_of_left = A[i-1]
                else: max_of_left = max(A[i-1], B[j-1])

                if (m + n) % 2 == 1:
                    return max_of_left

                if i == m: min_of_right = B[j]
                elif j == n: min_of_right = A[i]
                else: min_of_right = min(A[i], B[j])

                return (max_of_left + min_of_right) / 2.0

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        return self.median(nums1,nums2)
        
if __name__ == '__main__':
    nums1 = [10,20,30,40,50]
    nums2 = [1,15,35,45,55,65]
    print(Solution().findMedianSortedArrays(nums1,nums2))
