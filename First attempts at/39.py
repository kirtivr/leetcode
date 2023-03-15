from typing import List, TypedDict
import pdb

class Target(TypedDict):
    target: int
    choices: List[List[int]]

class Solution:
    def BottomUpComputeTargets(self, c: List[int], t: int, dp: Target):
        for target in range(1, t + 1):
            for idx, choice in enumerate(c):
                if target < choice:
                    break
                # Know how to get this target.
                if target - choice in dp:
                    # List of all routes to target - choice.
                    # Essentially a list of lists.
                    for sub in dp[target - choice]:
                        #print(f'target = {target} choice = {choice} target - choice = {target-choice} sub = {str(sub)} dp[target-choice] = {dp[target-choice]}')
                        found = False
                        for sub_idx, num in enumerate(sub):
                            # Insert in the right spot.
                            if num >= choice:
                                found = True
                                break
                        to_append = None
                        if found:
                            to_append = sub[:sub_idx]+[choice]+sub[sub_idx:]
                        else: # choice is greater than all subs. Insert at the end.
                            to_append = sub + [choice]
                        if target in dp and to_append not in dp[target]:
                            dp[target].append(to_append)
                        elif target not in dp:
                            dp[target] = [to_append]

                        #print(f'post_append - dp[{target}] = {dp[target]} to_append = {to_append}')


                if target - choice == 0:
                    #print(f'found target = {target}')
                    to_append = [choice]
                    if target not in dp:
                        dp[target] = [to_append]
                    else:
                        dp[target].append(to_append)
                    #print(dp)
        #print(dp)
                        
        return [] if t not in dp else dp[t]

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        dp = Target()
        candidates = sorted(candidates)
        return self.BottomUpComputeTargets(candidates, target, dp)
        
if __name__ == '__main__':
    x = Solution()
#    c = [2, 3, 5]
#    t = 8
    c = [2, 3, 6, 7]
    t = 7
    print(x.combinationSum(c, t))
