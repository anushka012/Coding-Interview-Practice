class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if len(strs) == 0:
            return ("")
        
        elif len(strs) == 1:
            return (strs[0])
        
        prefix = strs[0]
        plen = len(prefix)
        
        for i in strs[1:]:
            
            while prefix != i[0: plen]:
                prefix = prefix[0: (plen-1)]
                plen -= 1
                
                if plen == 0:
                    return("")
                
                
        return prefix