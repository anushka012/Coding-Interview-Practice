class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        N = len(nums) //length of the array
        if N <= 1 :
            return N
        
        i, j = 1,1
        
        while i < N:
            if nums[i] != nums[i-1]: //check for unique element 
                nums[j] = nums[i]
                j+=1
            i +=1 
        return j