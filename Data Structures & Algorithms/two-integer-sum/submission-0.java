class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            int n = nums[i];
            int required = target - n;
            if (map.containsKey(required)) {
                return new int[]{map.get(required), i};
            }
            map.put(n, i);
        }

        return null;
    }
}
