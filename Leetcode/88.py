class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return
        
        j = 0
        for i in range(m,m+n):
            nums1[i] = nums1[j]
            j = j + 1

        ptr1 = m
        ptr2 = 0
        i = 0
        rem1 = m
        rem2 = n
        
        while ptr1 < m+n and ptr2 < n and (rem1 > 0 or rem2 > 0):

            if rem1 > 0 and rem2 > 0:
                
                n1 = nums1[ptr1]
                n2 = nums2[ptr2]

                if n2 < n1:
                    ptr2 = ptr2 + 1
                    nums1[i] = n2
                    rem2 = rem2 - 1
                    
                elif n1 <= n2:
                    ptr1 = ptr1 + 1
                    nums1[i] = n1
                    rem1 = rem1 - 1
            elif rem1 > 0 and rem2 == 0:
                n1 = nums1[ptr1]
                nums[i] = n1
                ptr1 = ptr1 + 1
                rem1 = rem1 - 1
            else:
                n2 = nums1[ptr2]
                nums[i] = n2
                ptr2 = ptr2 + 1
                rem2 = rem2 - 1
            
