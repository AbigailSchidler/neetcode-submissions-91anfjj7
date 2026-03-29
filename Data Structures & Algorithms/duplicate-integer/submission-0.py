class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        inside = []
        for i in nums:
            if i in inside:
                return True
            inside.append(i)
        return False