class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i =0
        j=0
        to=0
        res =float('inf')
        while j < len(nums):
            to +=nums[j]
            while to >= target:
                res = min(res, j - i + 1)
                to -= nums[i]
                i += 1
            
            j+=1

        return 0 if res == float('inf') else res
