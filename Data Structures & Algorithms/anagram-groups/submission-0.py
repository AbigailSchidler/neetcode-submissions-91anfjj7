class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # my attempt was really close to hash table
        """
        sublists = []
        map = {}
        for s in strs:
            count_chars = [0] * 26
            for c in s:
                count_chars[ord(c) - ord('a')] += 1
            map[s] = count_chars
        
        return sublists
        """
        res = defaultdict(list)
        for s in strs:
            count_chars = [0] * 26
            for c in s:
                count_chars[ord(c) - ord('a')] += 1
            res[tuple(count_chars)].append(s)
        return list(res.values())