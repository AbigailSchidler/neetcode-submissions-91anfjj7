class Solution {
    public int singleNumber(int[] nums) {
        ArrayList<Integer> l= new ArrayList<>();

        for (int n : nums) {
            if (l.contains(n)) {
                l.remove(Integer.valueOf(n));
            } else {
                l.add(n);
            }
        }

        return l.get(0);
    }
}
