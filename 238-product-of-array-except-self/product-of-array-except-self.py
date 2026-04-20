class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr = [1]*len(nums)
        for i in range(1,len(nums)):
            arr[i] = nums[i-1]*arr[i-1]
        r = 1
        for i in range(len(nums)-1,-1,-1):
            arr[i] *= r
            r *= nums[i]

        
        
        return arr