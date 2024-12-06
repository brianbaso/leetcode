class Solution:
    # use a hashmap to track the previously visited num's index
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create a hashmap that keeps track of each index as you iterate
        # through the list
        d = {}
        for i, num in enumerate(nums):
            match = target - num
            if (match in d):
                return [i, d[match]]
            d[num] = i
