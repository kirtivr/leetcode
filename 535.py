class Codec:
    # using base64 encoding
    def __init__(self):
        self.refTable = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'

    def convertBinary(self, binStr):
        num = 0
        for b in binStr:
            num = num * 2 + (1 if b == '1' else 0)
        return num
    
    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """

        binaryRep = ''.join(format(ord(c), '08b') for c in longUrl)
        encodedStr = ''
        
        while(len(binaryRep) >= 6):
            binStr = binaryRep[:6]
            ch = self.convertBinary(binStr)
            encodedStr = encodedStr + self.refTable[ch]
            binaryRep = binaryRep[6:]

        
        paddingCh = 0 if len(binaryRep) == 0 else 6 - (len(binaryRep) % 6)

        if paddingCh > 0:
            binStr = binaryRep + ''.join('0' for x in range(paddingCh))
            ch = self.convertBinary(binStr)
            encodedStr = encodedStr + self.refTable[ch]
            
        for x in range(paddingCh):
            encodedStr = encodedStr + '='

        return encodedStr
        
    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        
        longUrl = ''
        binStr = ''

        for ch in shortUrl:
            if ch >= 'A' and ch <= 'Z':
                num = ord(ch) - ord('A')
            elif ch >= 'a' and ch <= 'z':
                num = ord(ch) - ord('a') + 26
            elif ch >= '0' and ch <= '9':
                num = ord(ch) - ord('0') + 52
            elif ch == '+':
                num = 62
            elif ch == '/':
                num = 63
            elif ch == '=':
                break
            binStr = binStr + format(num,'06b')

        while len(binStr) >=8:
            currBin = binStr[:8]
            num = self.convertBinary(currBin)
            longUrl = longUrl + chr(num)
            binStr = binStr[8:]

        return longUrl
        
            
# Your Codec object will be instantiated and called as such:
url = "https://leetcode.com/problems/design-tinyurl"
codec = Codec()
print(codec.decode(codec.encode(url)))
