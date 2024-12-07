class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        # iterate through array
        # use left and right pointer
        # L starts at first number
        # R starts at next number
        # while R+1 == num+1
        # if R+1 != num+1
        # if R != L, add L + "->" + R to list
        # else add R to list
        # Set L to R+1
        # if R inbounds, set R to R+2
        # Go back through while loop
        if len(nums) == 0:
            return []
        elif len(nums) == 1:
            return [str(nums[0])]

        L = 0
        result = []
        for R, num in enumerate(nums):
            at_end = R == len(nums)-1

            if at_end or nums[R+1] != num+1:
                if L != R:
                    result.append(f"{nums[L]}->{nums[R]}")
                else:
                    result.append(f"{nums[L]}")

                if not at_end:
                    L = R+1

        return result
