#!/usr/bin/env python
import time
import pdb
import sys
import copy
from typing import List, TypedDict

class Solution:
    def add(self, out: List[str]) -> str:
        # Start from the last column of the last row and sum up vertically.
        sum_row = ''
        carry = 0
        for row_idx in range(len(out) - 1, -1, -1):
            if len(out[row_idx]) < len(out[-1]):
                out[row_idx] = ('0' * (len(out[-1]) - len(out[row_idx]))) + out[row_idx]
        for col_idx in range(len(out[-1]) - 1, -1, -1):
            col_sum = 0
 #           print(f'add numbers for column {col_idx}')
            for row_idx in range(len(out) - 1, -1, -1):
                if len(out[row_idx]) - 1 < col_idx:
                    break                    
                num = int(out[row_idx][col_idx])
                col_sum += num
            col_sum += carry
            p = col_sum % 10
            sum_row = str(p) + sum_row            
            carry = col_sum // 10
#            print(f'p = {p} sum_row = {sum_row} carry = {carry} col_sum = {col_sum}')

        sum_row = str(carry) + sum_row if carry > 0 else sum_row
        return sum_row
            
    def multiply(self, num1: str, num2: str) -> str:
        out = ['' for j in range(len(num2))]
        row = 0
#        pdb.set_trace()
        for b_idx in range(len(num2) - 1, -1, -1):
            b_num = int(num2[b_idx])
            carry = 0
            for a_idx in range(len(num1) - 1, -1, -1):
                a_num = int(num1[a_idx])
                mul = (a_num * b_num + carry)
                p = mul % 10
                carry = mul // 10
                out[row] = str(p) + out[row]
#               print(out)
            out[row] = out[row] + ('0' * row)
            out[row] = str(carry) + out[row] if carry > 0 else out[row]
            row += 1
        
#        print(out)
        ret = self.add(out).lstrip('0')
        return(ret if len(ret) > 0 else '0')
if __name__ == '__main__':
    x = Solution()
    start = time.time()
    num1 = "140"
    num2 = "721"
    print(x.multiply(num1, num2))
    end = time.time()
    elapsed = end - start
    print (f'time elapsed = {elapsed}')
