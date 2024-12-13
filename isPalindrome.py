class Solution:
    def isPalindrome(self, s: str) -> bool:
        x = ""
        for char in s:
            if char.isalnum():
                x += char.lower()

        L, R = 0, 0
        if len(x) % 2 == 0:
            L = len(x) // 2 - 1
        else:
            L = len(x) // 2

        R = len(x) // 2


        while L >= 0 and R <= len(x) - 1:
            if x[L] != x[R]:
                return False
            L -= 1
            R += 1

        return True
