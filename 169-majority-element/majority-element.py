class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = {}
        # for i in nums:
        #     c[i] = c.get(i,0)+1
        # for key in c:
        #     if c[key] > len(nums) // 2:
        #         return key
        # return -1
        for i in nums:
            c[i] = c.get(i,0) + 1
        for  key  in c:
            if c[key] > len(nums) // 2:
                return key
        return -1
        