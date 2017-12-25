class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def getPermutations(current,remaining):
            if len(current) == 0 or len(remaining) == 0:
                return []

            out = []
            N = len(remaining)
            orig = remaining
            #print(remaining)
            
            for i in range(N):
                ch = remaining[i]
                remaining = remaining[:i] + remaining[i+1:]
                p = getPermutations(current[1:],remaining)
                if len(p) > 0:
                    for x in p:
                        perm = [ch]
                        perm.extend(x)
                        out.append(perm)
#                    print('perm '+str(perm))
#                    print('ch = '+str(ch))
                else:
#                    print('ch = '+str(ch)+' ..single')
                    out.append([ch])
#                print('out = ' +str(out))
                remaining = orig

            return out
        
        out = getPermutations(nums[:],nums[:])
        return out

if __name__ == '__main__':
    nums = [0,-1,1]
    print(Solution().permute(nums))
