class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_count = {}
        for c in s:
            if c in char_count.keys():
                char_count[c] += 1
            else:
                char_count[c] = 1
        
        for c in t:
            if (c in char_count.keys()) and (char_count[c] > 0):
                char_count[c] -= 1
            else:
                return False
        
        for c in s:
            if char_count[c] != 0:
                return False

        return True