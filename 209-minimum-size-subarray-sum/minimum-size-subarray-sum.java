class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        int res= Integer.MAX_VALUE;
        int n = nums.length;
        int high = 0;
        int low = 0;
        int sum = 0;
        int len = 0;
       
         while(high < n){
            sum += nums[high];

            while(sum >= target){
                 len = high - low + 1;
             res = Math.min(len, res);
             sum -= nums[low];
                low++;
            }
            high++;
         }
        // return res == Integer.MAX_VALUE ? 0 : res;
        if(res == Integer.MAX_VALUE){
            return 0;
        }
        return res;

    }
}