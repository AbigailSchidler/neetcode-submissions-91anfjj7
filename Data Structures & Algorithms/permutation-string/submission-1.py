class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        c1, c2 = [0] * 26, [0] * 26
        for i in range(len(s1)):
            c1[ord(s1[i]) - ord('a')] += 1
            c2[ord(s2[i]) - ord('a')] += 1
        l, r = 0, len(s1) - 1
        while r < len(s2):
            if c1 == c2:
                return True
            c2[ord(s2[l]) - ord('a')] -= 1
            l, r = l + 1, r + 1
            if r < len(s2):
                c2[ord(s2[r]) - ord('a')] += 1
        return False