from typing import List, Optional, Tuple, Dict
import pdb
import ast
import sys
from functools import cmp_to_key
import time

def make_comparator(less_than):
    def compare(x, y):
        if less_than(x, y):
            return -1
        elif less_than(y, x):
            return 1
        else:
            return 0
    return compare

class Solution:
    def findLCM(self, divisor1: int, divisor2: int) -> int:
        max_el = divisor1 * divisor2
        if divisor1 % divisor2 == 0:
            return divisor1
        elif divisor2 % divisor1 == 0:
            return divisor2
        mn_d = min(divisor1, divisor2)
        mx_d = max(divisor1, divisor2)
        start = mn_d * (mx_d//mn_d)
        while start <= max_el:
            #print(f'trying {start} for LCM')
            if start % divisor1 == 0 and start % divisor2 == 0:
                return start
            start += mn_d

    def findTotalElements(self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int, lcm: int, min_el: int, max_el: int) -> int:
        if min_el > max_el:
            return None
        total = min_el + ((max_el - min_el)//2)
        mult_lcm = total//lcm
        # If len(arr1) is less than the elements that can ONLY be added to arr1 we need to skip
        # more elements.
        fits_only_in_arr1 = total//divisor2 - mult_lcm
        leftover_arr1 = max(uniqueCnt1 - fits_only_in_arr1, 0)

        fits_only_in_arr2 = total//divisor1 - mult_lcm
        leftover_arr2 = max(0, uniqueCnt2 - fits_only_in_arr2)

        # Elements that can fit in either array (those neither divisible by d1 or d2)
        fits_in_either = total - mult_lcm - fits_only_in_arr1 - fits_only_in_arr2                
        #pdb.set_trace()
        if fits_in_either <  (leftover_arr1 + leftover_arr2):
            return self.findTotalElements(divisor1, divisor2, uniqueCnt1, uniqueCnt2, lcm, total + 1, max_el)
        elif fits_in_either > (leftover_arr1 + leftover_arr2):
            return self.findTotalElements(divisor1, divisor2, uniqueCnt1, uniqueCnt2, lcm, min_el, total - 1)
        else:
            can_be_smaller = (self.findTotalElements(divisor1, divisor2, uniqueCnt1, uniqueCnt2, lcm, min_el, total - 1))
            return total if can_be_smaller == None else can_be_smaller

    def minimizeSet(self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:
        # Find elements divisible by both divisor1 and divisor2.
        print(f'divisor1 = {divisor1} divisor2 = {divisor2} arr1 size = {uniqueCnt1} arr2 size = {uniqueCnt2}')
        lcm = self.findLCM(divisor1, divisor2)

        total = uniqueCnt1 + uniqueCnt2
        max_elements = total * 2
        min_elements = total
        return self.findTotalElements(divisor1, divisor2, uniqueCnt1, uniqueCnt2, lcm, min_elements, max_elements)
            
    def minimizeSet2(self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:
        arr1 = []
        arr2 = []
        common_but_add_to_1 = []
        curr = 1
        while len(arr1) < uniqueCnt1 or len(arr2) < uniqueCnt2:
            if len(arr1) < uniqueCnt1:
                if curr % divisor1 != 0:
                    arr1.append(curr)
                    if curr % divisor2 != 0:
                        common_but_add_to_1.append(curr)
                    curr += 1
                    continue

            if len(arr2) < uniqueCnt2:
                if curr % divisor2 != 0:
                    arr2.append(curr)
                    curr += 1
                    continue
                elif curr % divisor1 != 0 and len(arr1) >= uniqueCnt1 and len(common_but_add_to_1) > 0:
                    print(f'here common1 = {common_but_add_to_1} curr = {curr}')
                    # We can add curr to arr1 if we can find an element in arr1 which is also OK to add
                    # to arr2.
                    elem = common_but_add_to_1.pop()
                    arr2.append(elem)
                    arr1.append(curr)
            curr += 1

        #print(arr1)
        #print(arr2)
        return max(arr1[-1] if len(arr1) > 0 else 0, arr2[-1] if len(arr2) > 0 else 0)

if __name__ == '__main__':
    x = Solution()
    start = time.time()
    with open('6295_in', 'r') as f:
        divisor1 = ast.literal_eval(f.readline())
        divisor2 = ast.literal_eval(f.readline())
        uniqueCnt1 = ast.literal_eval(f.readline())
        uniqueCnt2 = ast.literal_eval(f.readline())
        print(x.minimizeSet(divisor1, divisor2, uniqueCnt1, uniqueCnt2))
    end = time.time()
    elapsed = end - start
    print(f'time elapsed: {elapsed}')