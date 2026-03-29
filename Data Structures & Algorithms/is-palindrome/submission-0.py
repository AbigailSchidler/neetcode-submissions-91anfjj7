class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphaNum = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        front = 0
        back = len(alphaNum) - 1
        while front < back:
            if alphaNum[front] != alphaNum[back]:
                return False
            front += 1
            back -= 1
        return True