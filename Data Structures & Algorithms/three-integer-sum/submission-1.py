class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        # sorting the array to set up two-pointer settings
        nums.sort()
        # iterate through smallest number
        for i in range(len(nums)):
            # prevents duplication
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # two pointer
            j = i + 1
            k = len(nums) - 1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total < 0:
                    j += 1
                elif total > 0:
                    k -= 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    # prevent duplication
                    while nums[j] == nums[j-1] and j < k:
                        j += 1
        return res