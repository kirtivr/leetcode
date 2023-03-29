class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.strip()
        N = len(s)
        ls = []
        j = 0
        
        for i in range(N):
            if i > 0 and s[i] == ' ' and s[i-1] == ' ':
                continue
            else:
                ls.append(s[i])
                j += 1

        s = ls
        N = len(s)
        
        def reverse(st,end):
            mid = st + (int(end - st + 0.5)//2)
            for i in range(mid - st):
                s[st+i],s[end-i-1] = s[end-i-1],s[st+i]
        
        reverse(0,N)
        s.append(' ')
        N += 1
        
        prev = None
        for i in range(N):
            if s[i] == ' ':
                if prev == None:
                    reverse(0,i)
                else:
                    #print('reversing indices '+str(prev+1) +' to '+str(i))
                    reverse(prev+1,i)
                prev = i

        #print(s)
        return "".join(s[:-1])


if __name__ == '__main__':
    s = "the sky is blue"
    s = "hi!"
    #s = " "
    #s = "   a   b "
    print(Solution().reverseWords(s))
