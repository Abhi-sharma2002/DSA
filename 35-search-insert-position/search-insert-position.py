class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
            l = 0
            j = len(nums) -1
            while l <=j:
                mid = (l +j) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    j = mid - 1
                else:
            
                   l = mid + 1
            return l
            
                   
                    


        