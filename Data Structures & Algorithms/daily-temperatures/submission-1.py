class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n

        # iterate backwards through temperatures (i is lower index)
        for i in range(n - 2, -1, -1):
            # set j to element after i (starting at last element in temps)
            j = i + 1
            # while temps after i are lower than temp at i
            while j < n and temperatures[j] <= temperatures[i]:
                # if there are no elements higher than at j
                # (aka) it was processed as being the highest temp at that
                # index and after
                if res[j] == 0:
                    j = n
                    break
                # otherwise, add to j to get to the placement of temp higher
                # than temp at j
                j += res[j]
            
            # if not out of bounds AND temp at j was found to be higher than i
            if j < n:
                # dist between indices
                res[i] = j - i
        return res