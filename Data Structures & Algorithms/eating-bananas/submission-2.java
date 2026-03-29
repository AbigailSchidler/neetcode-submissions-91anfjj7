class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        int l = 1;
        int r = piles[0];
        for (int i = 1; i < piles.length; i++) {
            if (r < piles[i]) {
                r = piles[i];
            }
        }
        int res = r;

        while (l <= r) {
            int k = (l + r) / 2;

            int totalTime = 0;
            for (int pile : piles) {
                totalTime += (int) Math.ceil((double)pile/k);
            }

            if (totalTime <= h) {
                res = k;
                r = k - 1;
            } else {
                l = k + 1;
            }
        }

        return res;
    }
}
