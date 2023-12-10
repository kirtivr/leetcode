from typing import List, Optional, Tuple, Dict
import pdb
import ast
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
    def expandExponentiationWithModulo(self, base, original_base, exponent, modulus):
        if exponent == 1:
            return base % modulus

        multiply_once = (base * original_base) % modulus
        return self.expandExponentiationWithModulo(multiply_once, original_base, exponent - 1, modulus)

    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        out = []
        for group_i in range(len(variables)):
            group = variables[group_i]
            a_i = group[0]
            b_i = group[1]
            c_i = group[2]
            m_i = group[3]

            inner = self.expandExponentiationWithModulo(a_i % 10, a_i % 10, b_i, 10)
            result = self.expandExponentiationWithModulo(inner % m_i, inner % m_i, c_i, m_i)
            #print(f'for group {group} inner = {inner} result = {result}')
            if result == target:
                out.append(group_i)
        return out

if __name__ == '__main__':
    x = Solution()
    start = time.time()
    with open('100155.text', 'r') as f:
        edges = ast.literal_eval(f.readline())
        target = ast.literal_eval(f.readline())
        #print(edges)
        print(x.getGoodIndices(edges, target))
    end = time.time()
    elapsed = end - start
    print(f'time elapsed: {elapsed}')