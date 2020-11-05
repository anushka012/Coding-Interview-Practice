class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if s=='':
            return 0
        
        s = s.split()
        if not s:
            return 0
        
        return len(s[-1])