class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # narrow down on row first (first element of row via bs)
        # once row is chosen, continue bs as normal on that row
        t, b = 0, len(matrix) - 1
        while t <= b:
            mid = t + ((b - t) // 2)
            num = matrix[mid][0]
            if num == target:
                return True
            elif num > target:
                b = mid - 1
            else:
                t = mid + 1
        row = 0
        if target < matrix[b][0]:
            row = t
        else:
            row = b
        l, r = 0, len(matrix[row]) - 1
        while l <= r:
            mid = l + ((r - l) // 2)
            num = matrix[row][mid]
            if num == target:
                return True
            elif num > target:
                r = mid - 1
            else:
                l = mid + 1
        return False