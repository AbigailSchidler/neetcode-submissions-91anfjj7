class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
        sort_counts = {k: v for k, v in sorted(counts.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)}
        res = list()
        for num in sort_counts:
            if len(res) == k:
                return res
            res.append(num)
        return res