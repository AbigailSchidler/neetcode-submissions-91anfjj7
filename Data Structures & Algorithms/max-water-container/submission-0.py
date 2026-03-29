class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        for i in range(len(heights) - 1):
            for j in range(i + 1, len(heights)):
                h = min(heights[i], heights[j])
                w = j - i
                area = h * w
                if area > maxArea:
                    maxArea = area
        return maxArea