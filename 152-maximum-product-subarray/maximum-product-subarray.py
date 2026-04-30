class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxsum = 0
        prefix = 1
        suffix = 1
        
        for i in range(len(nums)):
            if len(nums) == 1:
                return nums[i]
            if prefix == 0:
                prefix =1
            if suffix == 0:
                suffix =1
            
                
            prefix = prefix * nums[i]
            suffix = suffix * nums[len(nums)-i-1]
            maxsum = max(maxsum , max(prefix, suffix))

        return maxsum


        