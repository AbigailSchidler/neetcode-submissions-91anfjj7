class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        found = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in found:
                return [found[diff], i]
            found[nums[i]] = i
        return [-1, -1]