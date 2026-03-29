class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # expand window until all chars are found (r += 1)
        # once all chars are found minimize window until a char is missing (l += 1)
        # repeat
        if len(t) > len(s):
            return ""
        res = ""
        length = float("infinity")
        l = 0
        count = [0] * 52
        for c in t:
            if c.isupper():
                count[ord(c) - ord('A') + 26] += 1
            else:
                count[ord(c) - ord('a')] += 1
        for r in range(len(s)):
            if s[r].isupper():
                count[ord(s[r]) - ord('A') + 26] -= 1
            else:
                count[ord(s[r]) - ord('a')] -= 1
            found = True
            for c in count:
                if c > 0:
                    found = False
            while found:
                if length > len(s[l:r+1]):
                    res = s[l:r+1]
                    length = len(s[l:r+1])
                if s[l].isupper():
                    count[ord(s[l]) - ord('A') + 26] += 1
                else:
                    count[ord(s[l]) - ord('a')] += 1
                l += 1
                for c in count:
                    if c > 0:
                        found = False
        return res