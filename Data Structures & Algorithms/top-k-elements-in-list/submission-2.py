class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        elements = {}
        for num in nums:
            if num in elements:
                elements[num] += 1
            else:
                elements[num] = 1
        most_freq = sorted(elements.items(), key=lambda x: x[1], reverse=True)
        res = []
        for num, val in most_freq:
            res.append(num)
            if len(res) == k:
                return res
        return res