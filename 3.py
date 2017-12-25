class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        chPos = {}
        seq = [ 1 for i in range(len(s)) ]

        for idx, ch in enumerate(s):
            if ch in chPos:
                lastSeen = chPos[ch]
                if seq[idx-1] + 1 > idx - lastSeen:
                    seq[idx] = max(idx - lastSeen, 1)
                else:
                    seq[idx] = seq[idx - 1] + 1
            else:
                if idx != 0:
                    seq[idx] = seq[idx-1] + 1


            chPos[ch] = idx

        maxSeq = 0
        
        for num in seq:
            if num > maxSeq:
                maxSeq = num

        return maxSeq


if __name__ == '__main__':
    s = "pwwkew"
    Solution().lengthOfLongestSubstring(s)
