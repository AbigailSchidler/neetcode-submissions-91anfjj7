class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # brute force approach
        '''
        maxArea = 0
        for i in range(len(heights) - 1):
            for j in range(i + 1, len(heights)):
                h = min(heights[i], heights[j])
                w = j - i
                area = h * w
                if area > maxArea:
                    maxArea = area
        return maxArea
        '''
        maxArea = 0
        l, r = 0, len(heights) - 1
        while l < r:
            h = min(heights[l], heights[r])
            w = r - l
            area = h * w
            if area > maxArea:
                maxArea = area
            if heights[l] >= heights[r]:
                r -= 1
            else:
                l += 1
        return maxArea