class Solution {
    public int maxProfit(int[] prices) {
        int min =Integer.MAX_VALUE;
        int max = 0;
        for(int i =0;i<=prices.length-1;i++){
            if(prices[i] < min){
                min = prices[i];
            }else{
                int cp = prices[i] - min;
                max = Math.max(max , cp);
            }
        }
        return max;

    }
}