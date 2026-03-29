class Solution {
    public int maxSubArray(int[] nums) {
        int n = nums.length;
        int res = nums[0];
        for (int i = 0; i < n; i++) {
            int curr = 0;
            for (int j = i; j < n; j++) {
                curr += nums[j];
                res = Math.max(res, curr);
            }
        }
        return res;
    }
}
