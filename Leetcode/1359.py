from typing import List, Optional, Tuple, Dict
from functools import cache
import pdb
import time

class Solution:
    @cache
    def countPickupsAndDeliveries(self, P: int, D: int) -> int:
        N = P + D
        if P == 0 and D == 0:
            return 0
        elif P == 1 and D == 0:
            return 1
        elif P == 0 and D == 1:
            return 1
        elif P == 0:
            return (D * self.countPickupsAndDeliveries(P, D - 1))  % 1000000007
        elif P == 1 and D == 1:
            return 3
        if D == 0:
            return N * (self.countPickupsAndDeliveries(P - 1, 1)) % 1000000007
        else:
            # Pick P
            x = (P * self.countPickupsAndDeliveries(P - 1, D + 1)) % 1000000007
            # Pick D
            y = (D * self.countPickupsAndDeliveries(P, D - 1)) % 1000000007
            return x + y

    def countOrders(self, n: int) -> int:
        return self.countPickupsAndDeliveries(n, 0)

if __name__ == '__main__':
    x = Solution()
    start = time.time()
    n = 18
    print(x.countOrders(n))
    end = time.time()
    elapsed = end - start
    print(f'time elapsed: {elapsed}')