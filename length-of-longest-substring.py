class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L, maxLen = 0, 0
        d = {}

        for R, char in enumerate(s):
            # d[char] < L checks to see if it is in d, BUT it got removed from
            # the window due to another duplicate char
            # in this case, we just update its latest occurance and add to currLen
            if char not in d or d[char] < L:
                d[char] = R
                maxLen = max(maxLen, (R+1) - L)
            else:
                L = d[char] + 1
                d[char] = R                    
        
        return maxLen
