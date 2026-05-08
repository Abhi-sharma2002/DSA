class Solution:
    def rever(self ,nums,i , j):
       
        while i < j:
            nums[i],nums[j] = nums[j],nums[i]
            i+=1
            j-=1



    def rotate(self, nums: List[int], k: int) -> None:
            i=0
            j=len(nums)
            k = k % len(nums)
            self.rever(nums, 0, len(nums)-1)
            self.rever(nums, 0,k-1)
            self.rever(nums , k , len(nums)-1)
        
            