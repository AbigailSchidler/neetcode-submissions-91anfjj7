class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        # sorts by position (highest position first)
        pair.sort(reverse=True)
        stack = []
        for p, s in pair:
            # mi / (mi/hr) = hr
            # stores the time left to reach destination in hr
            stack.append((target - p) / s)
            # case when there are at least two elements in stack
            # and the element just added (lower position)
            # has less time to reach destination than higher position
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                # pop acts as a way to merge cars together
                stack.pop()
        return len(stack)