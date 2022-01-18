class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if haystack == '' and needle == '':
            return 0
        elif needle not in haystack:
            return -1
        else:
            return haystack.index(needle)