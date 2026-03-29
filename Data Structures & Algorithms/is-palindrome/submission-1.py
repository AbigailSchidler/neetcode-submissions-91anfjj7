class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = [c for c in s.lower() if c.isalnum()]
        return clean == clean[::-1]