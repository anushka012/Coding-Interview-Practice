class Solution:
    def reverse(self, x: int) -> int:
        num = str(abs(x))
        num = num[::-1]
        output = int(num)
        
        if output >= 2**31 -1 or output <= -2**31:
            return 0
        
        elif x<0:
            return -1*output
        
        else:
            return output