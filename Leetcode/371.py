class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """

        res = 0
        carry = 0
        ctr = 0

        maxLen = 32
        mask = 0xFFFFFFFF
        a = a & mask
        b = b & mask
        
        while (a != 0 or b != 0) and ctr < maxLen:
            s = ( a & 1 ) ^ ( b & 1 ) ^ ( carry )
            carry = ( a & 1 ) & ( b & 1 ) | ( a & 1 ) & ( carry ) | ( b & 1 ) & ( carry )
            a = a >> 1
            b = b >> 1

            if s == 1:
                res = ((res | 1 << ctr ) & mask)
            ctr += 1
            
        if carry == 1:
            res = (( res ) | (1 << ctr)) & mask
        print(hex(res))
        print(hex(~res))
        print(hex(~res + 1))
        print(hex(res^mask))
        print(hex(~(res^mask)))
        if res > 0x7FFFFFFF:
            res = ~(res ^ mask)
        return res

if __name__ == '__main__':
    a = -18
    b = 16
    print(Solution().getSum(a,b))

            
