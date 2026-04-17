class Solution {
    public long maximumSubarraySum(int[] nums, int k) {
        HashMap<Integer,Integer> map = new HashMap<>();
        int low = 0;
       long maxi = 0;
long sum = 0;
        for(int i = 0;i<nums.length;i++){
            map.put(nums[i], map.getOrDefault(nums[i],0)+1);
            sum += nums[i];
        
        while(map.get(nums[i]) > 1 || i -low +1 >k){
            map.put(nums[low],map.get(nums[low])-1);
            sum-=nums[low];
            if(map.get(nums[low]) == 0){
                map.remove(nums[low]);
            }
            low++;
        }
        if(i-low +1 == k){
            maxi = Math.max(maxi , sum);
        }
       
        }
        return maxi;
    }
}