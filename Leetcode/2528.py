from collections import defaultdict
from typing import List, Optional, Tuple, Dict
from heapq import heappop, heappush, heapify, heapreplace
import pdb
import ast
import sys
from functools import cmp_to_key
import time

def compareRanges(range1, range2, stations):
    r1s = range1[0]
    r1e = range1[1]
    r2s = range2[0]
    r2e = range2[1]

    #r1 = sorted(stations[r1s:r1e + 1])
    #r2 = sorted(stations[r2s:r2e + 1])

    return stations[r1s:r1e + 1] < stations[r2s:r2e + 1]

class Range:
        def __init__(self, start, end, nums):
            self.pointer_to_global = nums
            self.start = start
            self.end = end

        def incrementRange(self):
            #print(self.pointer_to_global)
            for i in range(self.start, self.end + 1):
                self.pointer_to_global[i] += (1)
            #print(f' incremented range from {self.pointer_to_global[self.start : self.end + 1]}\n{self.pointer_to_global}')

        def __len__(self):
            return self.end - self.start + 1

        def lessThan(self, other):
            # Enclosed case.
            if self.start >= other.start and self.end <= other.end:
                #print('1')
                return False
            elif other.start >= self.start and other.end <= self.end:
                #print('2')
                return True

            # Non overlapping case.
            if self.start > other.end or other.start > self.end:
                result = compareRanges((self.start, self.end), (other.start, other.end), self.pointer_to_global)
                #if self.start == 3:
                    #print(f'3 {self} {other}')
                return result

            ls = min(self.start, other.start)
            rs = max(self.start, other.start)
            lno = (ls, rs - 1)

            le = min(self.end, other.end)
            re = max(self.end, other.end)
            rno = (le + 1, re)

            if self.start < other.start:
                result = compareRanges(lno, rno, self.pointer_to_global)
                #if self.start == 3:
                #    print(f'4: {self} {other} left non overlapping = {lno} right no = {rno}')
                return result
            else:
                result = compareRanges(rno, lno, self.pointer_to_global)
                #print('5')
                return result


        # Python uses a min-heap by default.
        def __lt__(self, other):
            result = self.lessThan(other)
            #if result == False and self.start == 3:
            #    print(f'{other} smaller than {self}')
            #elif self.start == 3:
            #    print(f'{self} smaller than {other}')
            return result

        def __gt__(self, other):
            return not (self.__lt__(other))

        def __repr__(self):
            return f'nums = {self.pointer_to_global[self.start : self.end + 1]} start = {self.start} end = {self.end}'

class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        lo = min(stations)
        hi = sum(stations) + k
        
        # Adding bunch of (r+1) 0s to left, and (r) 0s to right for handling corner cases.
        stations = [0]*(r) + stations + [0]*r
        res = lo
        
        def check(med):
            available = k
            ind = r                         # ind of our first city
            
            window = sum(stations[:2*r])    # Sliding window will store power of stations for city
                                            # initially it will have values from 0th station to (r-1) stn
            
			# This will store, in which city we have added station because of deficiency. 
			# Because we need to remove that val when that city is out of range.
            added = defaultdict(int)        
                                            
            while ind < len(stations)-r:
                window += stations[ind + r]
                #print(f'range = {stations[ind - r : ind + r + 1]} added = {added} window = {window}')
                
                if window < med:
                    diff = med-window
                    if diff>available:
                        #print(f'mid ({med}) - sum ({window}) ({diff}) > k ({available}), we cannot raise sum to match mid, so return False')
                        #print(added)
                        return False
                    #print(f'sum up to this point {window} < mid {med}, updating to increase ans[i + r]')
                    window+=diff
                    added[ind+r]=diff 
                    available-=diff
					
                window -= (stations[ind - r] + added[ind-r])
                ind+=1
            #print(added)
            return True
        
        while lo<=hi:                       # Typical Binary Search
            m = (lo + hi )//2
            #print(f'\nlo = {lo} hi = {hi} m = {m} res = {res} stations = {stations}\n')
            if check(m):
                res = m
                lo = m + 1
            else:
                hi = m-1
        return res

class Solution2:
    def check(self, mid, ans: List[int], r, k):
        sum = 0
        n = len(ans)

        # Find the total sum in "ans".
        # This would probably be a large number.
        for i in range(r):
            sum += ans[i]

        # For each index "i" we traverse in the range
        # i - r to i + r, adjust the range sum.
        # Note that for a range starting at "i", the sum
        # is the power at i.
        for i in range(n):
            # We go from (i - r) to (i + r), adding (i + r) and removing (i - r - 1) from the range.
            # If the new sum is lesser, that means element at (i + r) is smaller which means we should
            # increment that element.

            # What about the range from (0, r - 1)? We never seem to even out that range.
            # So this is a confusion about what range really means. Range is not a length, it is how many other elements
            # to the left AND to the right we need to consider. So, any range starting from index x ends at x + r.
            sum += ((ans[i + r] if i + r <= n - 1 else 0)
            - (ans[i - r - 1] if i - r - 1 >= 0 else 0))
            print(f'(range = {ans[i - r if i - r >= 0 else 0: i + r + 1 if i + r <= n - 1 else n - 1]} sum = {sum} mid = {mid}) mid - sum = {mid - sum} k = {k}')
            # Find any range sum which is less than the scan line, which we can increase to match the scan line.
            if mid > sum:
                if mid - sum > k:
                    print(f'mid - sum ({mid - sum}) > k ({k}), we cannot raise sum to match mid, so return False, which will reduce mid.')
                    return (False, k)
                
                # We always only increment the tail of the range. So every index gets incremented if the range that ends at that index
                # is less than mid.
                if i + r <= n - 1:
                    print(f'sum up to this point < mid, updating to increase ans[i + r] from {ans[i + r]} to {ans[i + r] + (mid - sum)}')
                    ans[i + r] += (mid - sum)

                k -= (mid - sum)
                sum = mid

        # If we got here that means:
        # we never saw a range sum which was more than k steps away from mid.
        # Note that k also reduces every time we make sum match mid.

        # This means that after the adjustments we made to ans[i + r], none of the range sums are less than mid.
        # So we need to see if we can increase mid, to further even out the range sums.

        # Where do we keep track of if we used up all the k iterations we had?
        return (True, k)

    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        l = 0
        h = k
        n = len(stations)

        # h is the total power across cities.
        for i in range(n):
            h += stations[i]

        ans = [stations[i] for i in range(n)]

        # l starts from 0.
        while l < h and k > 0:
            mid = l + (h - l)//2
            # mid = h//2
            # this is half of the total power.
            print(f'\nchecking with low = {l} mid = {mid} high = {h} ans = {ans}')
            # what are we checking for?
            (res, new_k) = self.check(mid, ans, r, k)
            k = new_k
            if k == 0:
                break
            if res:
                print(f'check True setting low to {mid + 1}')
                l = mid + 1
            else:
                print(f'check False setting high to {mid - 1}')
                h = mid - 1
        print(f'ans = {ans} low = {l} high = {h}')
        return l

    def maxPower2(self, stations: List[int], r: int, k: int) -> int:
        ranges = []
        effective_power = [0 for i in range(len(stations))]
        # First extract all the ranges.
        for i in range(len(stations)):
            start = 0
            end = len(stations) - 1
            if i - r > 0:
                start = i - r
            if i + r < len(stations) - 1:
                end = i + r
            for j in range(start, end + 1):
                effective_power[i] += stations[j]
            #print(f'i = {i} start = {start} end = {end}')
            gr = Range(start, end, effective_power)
            ranges.append(gr)

        heapify(ranges)
        print(len(effective_power))
        #print(ranges)
        #print('\t-------------------\t\n')
        for i in range(k):
            #print(f'\n{ranges}')
            #print('\n popping')
            #heapify(ranges)
            #print(ranges)
            top = ranges[0]
            #print(top)
            #print('\n incrementing')
            top.incrementRange()
            #print('\npushing')
            heapreplace(ranges, top)
        #print(effective_power)
        min_city = float("inf")
        for city in effective_power:
            min_city = min(min_city, city)

        return min_city

if __name__ == '__main__':
    x = Solution()
    start = time.time()
    with open('2528_tc.text', 'r') as f:
        stations = ast.literal_eval(f.readline())
        #print(n)
        r = ast.literal_eval(f.readline())
        k = ast.literal_eval(f.readline())
        #print(edges)
        print(x.maxPower(stations, r, k))
    end = time.time()
    elapsed = end - start
    print(f'time elapsed: {elapsed}')