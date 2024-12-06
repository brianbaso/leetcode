class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # get the length of nums
        # convert nums to a set
        # if the length changed in the set, return True
        return len(nums) != len(set(nums))


