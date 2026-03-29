class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        maxArea = 0
        stack = []

        for i in range(n + 1):
            # if loop reaches the end, or the current height is less/equal
            # last element in stack
            # calculate maxArea until stack is emptied
            while stack and (i == n or heights[stack[-1]] >= heights[i]):
                # pop next lowest height in stack
                height = heights[stack.pop()]
                # i if all bars in stack have been removed (aka) added to width
                # else diff between i and index of height - 1
                width = i if not stack else i - stack[-1] - 1
                maxArea = max(maxArea, height * width)
            # append such that last element is smallest height
            stack.append(i)
        return maxArea