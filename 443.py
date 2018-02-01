import pdb
class Solution:
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        N = len(chars)
        
        def analyse(chars):
            curr = 0
            i = 0
            
            while i < N:
                curr += 1
                j = i+1
                while j < N and chars[j] == chars[i]:
                    j += 1
                if j-i > 1:
                    curr += len(str(j-i))
                i = j

            return curr

        rle = analyse(chars)

        if  rle < N:
            i = 0
            while i < N:
                j = i+1
                while j < N and chars[j] == chars[i]:
                    chars[j] = ''
                    j += 1

                if j-i != 1:
                    ch = str(j-i)
                    for m in range(len(ch)):
                        chars[i+1] = ch[m]
                        i += 1                        
                i = j                
        j = 0
        while j < N:
            #print(chars)
            #pdb.set_trace()
            if chars[j].isnumeric():
                j += 1
            elif chars[j] != '':
                j += 1
            else:
                k = j
                while k < N and chars[k] == '':
                    k += 1
                if k < N:
                    chars[k],chars[j] = chars[j],chars[k]
                j += 1
        print(chars)
   
        return rle if rle < N else N
if __name__ == '__main__':
    #inp = ["a","a","b","b","c","c","c"]
    #inp = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
    #inp = ["a"]
    inp = ["V","V","V","V","X","X","U","(","(","(","(","(","(","+","q","3","G","G","G","G","G","G","w","-","z","z","A","A","k","k",">","j","j",".","j","j","j","j","j","I","I","R","R","c","$","$","u","&","(","w","w","~","~","~","~","~","4","q","q","k","#","j","j","<","<","<","<","a","a","a","a","a","@","K","K","X","5","_","_","{","{","{","{","T","T","U","U","#","#","#","#","#","#","#","#","8","2","a",",",",",",",",",",","}","}","o","j","=","=","(","A","&","&","e","e","e","e","e","e","R","R","R","T","T","a","a","a","S","S","a","a","-","4","S","S","S","X","{","7","7","7","7","7","9","C","*","*","F","E","o","7","d",".","f","f","f","f","f","J","J","J","Q","Q","Q","Q","w","w","w","q","q","a","o","#","#","#","#","#","#","'","'","c","Z","Z","d","e","p","X","9","9","9","9","9","9","p","p","H","H","H","~","~","$","$","$","]","F","l","l","l","k","e","6","6","A","*","p","<","<","h","h","V","V","V","}","}","8","8","G","m","m","m","m","5","W","N","d","d","d","d","b","b","b","y","y","y","b","k","k","k","o","_","_","R","R","R","R","V","V","q","1","1","B","B","B","B","6","P","P","Q","F","R","R","R","R",">","O","O","O","O","O","O","<","V","6","8","8","8","z","z","k",";",")","W","-","-","D","D","D","e","e","@"]
    #inp = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
    #inp = ["a","b","c","d","e","f","g","g","g","g","g","g","g","g","g","g","g","g","a","b","c"]

    print(Solution().compress(inp))
