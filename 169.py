class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        prev_num = 0
        freq = 0
        for num in nums:
            if num == prev_num:
                freq += 1
            else:
                prev_num = num
                freq = 1
            if freq > len(nums) / 2:
                return num

