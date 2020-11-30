class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        temp, i = 1,1
        while temp <= n:
            if temp == n:
                return True
            
            temp = 2**i
            i+=1
        return False
            
            