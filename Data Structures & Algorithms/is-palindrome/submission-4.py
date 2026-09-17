class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = "".join(char.lower() for char in s if char.isalnum())
        if a == a[::-1]:
            return True
        return False