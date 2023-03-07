from typing import List, Optional, Tuple, Dict
import pdb
from functools import cmp_to_key
import time


class Solution:
    def isPrime(self, n: int) -> bool:
        divisors = 0
        for div in range(2, n):
            if n % div == 0:
                divisors += 1
            if divisors > 0:
                return False
        return True

    def enumerateDividingPrimes(self, upto: int) -> int:
        if upto < 2:
            return []
        if upto == 2:
            return [2]
        if upto == 3:
            return [3]
        if self.isPrime(upto):
            return [upto]

        prime_factors = []
        for i in range(2, upto + 1):
            if self.isPrime(i) and upto % i == 0:
                return [i] + self.enumerateDividingPrimes(upto//i)

    def smallestValue(self, n: int) -> int:
        # Multiple would be up to n//2
        # Enumerate all primes.
        while True:
            primes = self.enumerateDividingPrimes(n)
            div = list(primes)
            #print(div)
            print(f'{n} {div}')
            S = 0
            for num in div:
                S += num
            if S >= n:
                return S
            n = S

if __name__ == '__main__':
    x = Solution()
    start = time.time()
    n = 15
    #n = 3
    #n = 4
    #n = 12
    #n = 16
    print(x.smallestValue(n))
    end = time.time()
    elapsed = end - start
    print(f'time elapsed: {elapsed}')