class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo = 0
        mid = 0
        hi = len(nums) - 1

        while lo <= hi:
            mid = (hi + lo) // 2

            if nums[mid] < target:
                lo = mid + 1

            elif nums[mid] > target:
                hi = mid - 1

            else:
                return mid
        
        return -1
