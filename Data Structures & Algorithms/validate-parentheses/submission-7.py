class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        matches = {'(': ')', '{': '}', '[': ']'}
        stack = []
        for i in range(len(s)):
            if s[i] in matches.keys():
                stack.append(s[i])
            elif len(stack) == 0:
                return False
            else:
                for k, v in matches.items():
                    if v == s[i] and stack.pop() != k:
                        return False
        return len(stack) == 0