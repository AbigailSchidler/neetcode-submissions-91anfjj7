class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # key: tuple anagram, val: list of anagrams
        anagrams = {}
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            if tuple(count) in anagrams:
                anagrams[tuple(count)].append(s)
            else:
                anagrams[tuple(count)] = [s]
        return list(anagrams.values())