class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        elif n == 2:
            return "11"
        
        s = "11"
        for i in range(2,n):
            count=1
            res = ""
            for j in range(len(s)):
                if j == len(s)-1:
                    res = res + str(count)+s[j]
                    break
                elif s[j] == s[j+1]:
                    count+=1
                else:
                    res= res+str(count)+s[j]
                    count=1