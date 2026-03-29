class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # dictionary that stores key: num value: curr count (default 0)
        count = {}
        # list of empty lists
        # where index of list represents the count
        # list at index 0 will ALWAYS be empty
        freq = [[] for i in range(len(nums) + 1)]

        # increments the count of each number that appears
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        # adds the number to the frequency
        # by appending to the bucket at the index
        # that matches cnt
        for num, cnt in count.items():
            freq[cnt].append(num)
        res = []
        # iterates through all buckets backwards (except index 0)
        # backwards because it'll start at highest freq
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
        return res
        
        