class Solution:
    def reverseBits(self, n: int) -> int:
        str = "{0:032b}".format(n)
        reversed = str[::-1]
        
        return int(reversed, 2)
        