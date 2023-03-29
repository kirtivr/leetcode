class Solution(object):
    def median(self, L, S):
        L_len, S_len = len(L), len(S)
        if S_len > L_len:
            L, S, L_len, S_len = S, L, S_len, L_len

        s_low, s_high, l_low, l_high = 0, S_len, 0, L_len

        med_i = ((S_len + L_len)//2) - 1 # 0 index match.
        s_i = (s_low + s_high)//2
        l_i = (l_low + l_high)//2

        # Establish a window of length med_i between L and S.
        # Later we will adjust the indices of the window as necessary.
        while s_i + l_i != med_i:
            print(f'si = {s_i} li = {l_i} median = {med_i}')
            diff = abs(med_i - (s_i + l_i))
            if s_i + l_i < med_i:
                if S[s_i] <= L[l_i] and s_i < S_len - 1:
                    s_i = min(S_len - 1, s_i + diff)
                else:
                    l_i = min(L_len - 1, l_i + diff)
            else:
                if S[s_i] >= L[l_i] and s_i != 0:
                    s_i = max(0, s_i - diff)
                else:
                    l_i = max(0, l_i - diff)

        print(f'here')
        # We have an established window of length med_i + 2 (1 indexed).
        # Adjust s_i and l_i until invariants hold.
        s_i_jmp = 2
        l_i_jmp = 2
        while True:
            # Maybe move S to the right.
            if S[s_i] < L[l_i]:
                if s_i == S_len - 1:
                    break
                if S[s_i + 1] < L[l_i]:
                    s_i = max(S_len - 1, s_i + s_i_jmp)
                    s_i_jmp *= 2
                    l_i_jmp = 2
                else:
                    break
            elif L[l_i] < S[s_i]:
                if l_i == L_len - 1:
                    break
                if L[l_i + 1] < S[s_i]:
                    l_i = max(L_len - 1, l_i + l_i_jmp)
                    l_i_jmp *= 2
                    s_i_jmp = 2
                else:
                    break

        print(f'si = {s_i} li = {l_i} S = {S[:s_i + 1]} L = {L[:l_i + 1]}')

        median = 0
        if (med_i + 1) % 2 == 0:
            if L[l_i] > S[s_i]:
                median = L[l_i]
                if l_i == 0:
                    median += S[s_i]
                else:
                    median = median + S[s_i] if S[s_i] > L[l_i - 1] else L[l_i - 1]
            else:
                median = S[s_i]
                if s_i == 0:
                    median += L[l_i]
                else:
                    median = median + L[l_i] if L[l_i] > S[s_i - 1] else S[s_i - 1]
            median = median / 2
        else:
            median = L[l_i] if L[l_i] > S[s_i] else S[s_i]

        return median

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
    nums1 = [1, 2]
    nums2 = [3, 4]
    nums1 = [0, 0]
    nums2 = [0, 0]
    print(Solution().findMedianSortedArrays(nums1,nums2))
