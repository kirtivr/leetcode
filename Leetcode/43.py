class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        if len(num1) > len(num2):
            num1,num2 = num2,num1
            
        arr1 = []
        for ch in num1:
            arr1.append(ord(ch) - ord('0'))

        arr2 = []
        for ch in num2:
            arr2.append(ord(ch) - ord('0'))
        result = []
        maxLen = max(len(arr1),len(arr2))
        out = []
        carry = 0
        
        for i in range(len(arr1)-1, -1, -1):
            num1 = arr1[i]
            carry = 0
            
            for j in range(len(arr2)-1 , -1, -1):
                while not(len(out) -1 >= j):
                    out.insert(0,0)
                    
                mult = carry + num1 *arr2[j] + out[j]
                    
                print('num1 = '+ str(num1)+ ' arr[j] = '+str(arr2[j])+ ' carry = '+ str(carry)+ ' out el was '+str(out[j])+' mult = '+str(mult))
                out[j] = int(mult%10)
                carry = int(mult/10 )

            if carry > 0:
                out.insert(0,carry)
            print(out) 
            result.insert(0,out[-1])
            print('res.. '+str(result))
            out = out[:-1]
            
        print('outside')
        print(out)
        for el in out:
            if el == 0:
                out = out[1:]
            else:
                break

        for i in range(len(out)-1, -1, -1):
            el = out[i]
            result.insert(0,el)
        
        print(result)

        final = ''
        for el in result:
            final = final + str(el)
        return final
    
if __name__ == '__main__':
    num1 = '1800'
    num2 = '9'
    print(Solution().multiply(num1,num2))
