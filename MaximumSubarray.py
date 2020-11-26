class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        maxsum = total = nums[0]
        
        for i in nums[1:]:
            total = max(i, total+i)
            maxsum = max(total, maxsum)
            
        return maxsum