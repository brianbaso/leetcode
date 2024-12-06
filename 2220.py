class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        # convert start, goal to binary
        # iterate through start from right to left 
        # make the lengths of both bits equal by padding zeros
        # if goal bit is different, copy start bit into it
        # every time a copy happens, add to count
        count = 0
        s = bin(start)[2:]
        g = bin(goal)[2:]

        # if goal is less bits than start, make them equal
        if len(s) > len(g) and len(s) - len(g) > 0:
            diff = len(s) - len(g)
            for i in range(diff):
                g = "0" + g

        elif len(g) > len(s) and len(g) - len(s) > 0:
            diff = len(g) - len(s)
            for i in range(diff):
                s = "0" + s

        i = len(s) - 1
        # assuming len(s) and len(g) are now equal
        while i >= 0:
            print(s, g)
            if s[i] != g[i]:
                count += 1
            i -= 1
        return count
