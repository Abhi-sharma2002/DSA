class Solution(object):
        def getMinDistance(self, nums, target, start):
            k = float('inf') 
            for i in range (0, len(nums)):
                if nums[i] == target:
                    if k > abs(i - start):
                        k = abs(i- start)
            return k


        