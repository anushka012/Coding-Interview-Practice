class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dict = {}
        
        for i in nums:
            if i not in dict:
                dict[i] = 1
                
            else:
                dict[i] += 1
                
        for key, val in dict.items():
            if val == 1:
                return key