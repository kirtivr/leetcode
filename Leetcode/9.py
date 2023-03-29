class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        x = abs(x)
        y = x
        count = 0
        
        while y > 0:
            y = int(y/10)
            count = count + 1

        print("Count is "+str(count))
        
        front = 1

        temp = count
        while temp > 1:
            front = front * 10
            temp = temp - 1

        print("Front is "+str(front))
        
        if count %2 == 0:
            items = int(count / 2)

            for i in range(items):
                st = x / front
                l = x % 10

                if st != l:
                    return False

                x = x % front
                x = int(x/10)
                front = front / 100

        
        elif count%2 == 1:
            items = int(count/2)
            
            print("iterations : "+str(items))

            for i in range(items):
                print ('x is '+str(x))
                st = int(x / front)
                l = x % 10
                print("st is "+str(st)+" l is "+str(l))
                if st != l:
                    return False

                x = x % front
                x = int(x/10)
                front = front / 100

        return True

if __name__ == '__main__':
    num = -2147447412

    if Solution().isPalindrome(num):
        print("Palindrome")

    else:
        print("Not Palindrome")
