class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for i, num in enumerate(nums):
            # avoid duplicates (if next num is same as last)
            if i > 0 and num == nums[i-1]:
                continue

            target = -num
            L, R = i+1, len(nums)-1

            while L < R:
                if nums[L] + nums[R] == target:
                    ans.append([num, nums[L], nums[R]])

                    curr_L = nums[L]
                    while nums[L] == curr_L and L < R:
                        L += 1

                    curr_R = nums[R]
                    while nums[R] == curr_R and L < R:
                        R -= 1

                elif nums[L] + nums[R] < target:
                    curr_L = nums[L]
                    while nums[L] == curr_L and L < R:
                        L += 1

                elif nums[L] + nums[R] > target:
                    curr_R = nums[R]
                    while nums[R] == curr_R and L < R:
                        R -= 1

        return ans
