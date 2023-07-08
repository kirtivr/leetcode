"""
The read4 API is already defined for you.

    @param buf4, a list of characters
    @return an integer
    def read4(buf4):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf4 = [' '] * 4 # Create buffer with enough space to store characters
read4(buf4) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf4) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf4) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""

class Solution:
    def __init__(self):
        self.buffer = []

    def copy_to_buffer(self, from_buf, to_buf, from_idx, n):
        for i in range(n):
            to_buf[from_idx] = from_buf[i]
            from_idx += 1

    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        chars_read = None
        total_read = 0
        read4buf = ['' for i in range(4)]
        buf_idx = 0
        to_copy = 0

        while n > 0 and (chars_read is None or chars_read != 0):
            if len(self.buffer) > 0:
                print(f'self.buffer = {self.buffer}')
                to_copy = min(len(self.buffer), 4, n)
                print(f'to_copy = {to_copy}')
                for i in range(to_copy):
                    read4buf[i] = self.buffer[i]
                self.buffer = self.buffer[to_copy:]
                self.copy_to_buffer(read4buf, buf, buf_idx, to_copy)
                buf_idx += to_copy
            else:
                chars_read = read4(read4buf)    
                to_copy = min(n, chars_read)
                self.copy_to_buffer(read4buf, buf, buf_idx, to_copy)
                buf_idx += to_copy

                if n < chars_read:
                    # We have read excess characters. Store them in the buffer.
                    for i in range(n, chars_read):
                        self.buffer.append(read4buf[i])

            n -= to_copy
            total_read += to_copy

        buf = buf[:total_read + 1]
        return total_read
