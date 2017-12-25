class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        ans = []
        N = len(candidates)
        table = {}
        
        def getCombinations(i, remaining, cand, current):
            if i > N-1 or remaining < 0:
                return

            print(i)
            
            temp = list(current)
            
            if remaining == 0:
                if temp not in ans:
                    ans.append(temp)

            temp.append(cand[i])
            getCombinations(i, remaining - cand[i],cand, temp)
            temp.pop()
                
            getCombinations(i+1, remaining, cand, temp)
            
        getCombinations(0,target,candidates,[])

        return ans

if __name__ == '__main__':
    
#    nums = [48,22,49,24,26,47,33,40,37,39,31,46,36,43,45,34,28,20,29,25,41,32,23]
#    target = 69

    nums = [2,3,6,7]
    target = 7
    print(Solution().combinationSum(nums,target))
            

        
