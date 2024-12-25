class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        R = 1
        remaining_chars = 0
        ls = 0
        d = {}

        for L, char in enumerate(s):
            for i in range(L, R):
