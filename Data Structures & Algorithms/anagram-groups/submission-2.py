class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # creates a dictionary where keys are count of chars as a tuple
        # and values are strings that have the same count of chars
        res = defaultdict(list)
        for s in strs:
            # creates the count array of fixed size
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            # appending the string to the list at tuple
            res[tuple(count)].append(s)
        # grabs all groupings of strings from dictionary and makes a
        # list for each
        return list(res.values())