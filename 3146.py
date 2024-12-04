class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        # iterate through s
        # for each char in s, get the index of it in t
        # subtract i from index of t and get abs
        # add abs to the total
        total, indicies = 0, {}
        for i, char in enumerate(t):
            indicies[char] = i
    
        for i, char in enumerate(s):
            total += abs(i - indicies[char])
        return total