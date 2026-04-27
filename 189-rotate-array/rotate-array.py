class Solution:
    def rever(self,nums, i, j):
        while i<j:
            nums[i],nums[j] = nums[j],nums[i]
            i+=1
            j-=1
        
    def rotate(self, nums: List[int], k: int) -> None:
        n=len(nums)
        k=k%n
        self.rever(nums , 0, n-1)
        self.rever(nums, 0 , k-1)
        self.rever(nums, k, n-1)
    

