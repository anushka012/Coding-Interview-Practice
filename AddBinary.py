class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_dec = 0
        b_dec = 0
        a = a[::-1]
        b = b[::-1]
        a = list(a)
        b = list(b)
        
        i = 0
        while i < len(a):
            if a[i] == '1':
                a_dec += 2**i  
            i+=1
            
        i=0   
        while i < len(b):
            if b[i] == '1':
                b_dec += 2**i
            i+=1
            
        return bin(a_dec + b_dec)[2:]