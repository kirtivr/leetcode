class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        mapping = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        ordered = ["I","V","X","L","C","D","M"]
        sub = {"I":"IV","X":"XL","C":"CD","M":"CM"}
        roman = ''
        
        def recurse(remaining,current):
            if remaining == 0:
                return current

            minKey = None
            for i in range(len(ordered)):
                val = mapping[ordered[i]]
                if remaining-val >= 0:
                    minKey = ordered[i]

            current = current+minKey
            
            N = len(current)

            if N>=4:
                #print(current[N-4:])
                #print(current[N-1]*4)
                if current[N-4:] == current[N-1]*4:
                    #print('current fixed from '+current)
                    # Subtractive notation case
                    current = current[:N-4] + sub[current[N-1]] 
                    #print(' to '+current)
            return recurse(remaining - mapping[minKey], current)

        return recurse(num,roman)


if __name__ == '__main__':
    num = 148
    print(Solution().intToRoman(num))
