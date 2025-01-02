class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) > 0 and nums[0] <= nums[len(nums) - 1]:
            return nums[0]
        elif len(nums) == 2:
            return min(nums[0], nums[1])
        
        lo = 0
        hi = len(nums) - 1

        while lo <= hi:
            mid = (hi + lo) // 2
            # [5, 1, 2, 3, 4]
            if nums[mid - 1] > nums[mid]:
                return nums[mid]

            elif nums[mid - 1] < nums[hi]:
                hi = mid - 1

            elif nums[mid - 1] > nums[hi]:
                lo = mid + 1
        
        return -1
            
