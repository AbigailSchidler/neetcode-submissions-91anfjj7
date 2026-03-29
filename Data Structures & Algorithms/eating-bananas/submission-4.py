class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # min and max rates
        l, r = 1, max(piles)
        # worst case set to max rate at r
        res = r
        while l <= r:
            # get mid speed
            k = (l + r) // 2
            totalTime = 0
            # get total time using k
            for p in piles:
                totalTime += math.ceil(float(p) / k)
            # case when k is acceptable (could be the answer but there may be a smaller k)
            if totalTime <= h:
                res = k
                r = k - 1
            # case when k does not meet the h requirement
            else:
                l = k + 1
        return res
            