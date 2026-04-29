class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_p =0
        for i in range(len(nums)):
            if i > max_p:
                return False
            
            max_p = max(max_p , i + nums[i])
        return True

        