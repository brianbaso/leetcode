class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # keep track of the subarray sum before num
        # discard it if its <= 0, since it adds nothing to max_sum
        # keep track of max_sum

        max_sum, curr_sum = 0, 0

        for num in nums:
            if num + curr_sum > 0:
                if num + curr_sum > max_sum:
                    max_sum = num + curr_sum
                curr_sum += num

            else:
                curr_sum = 0
        
        return max_sum if max(nums) > 0 else max(nums)
