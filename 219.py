class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # create a hashmap of the most recent index of each num
        # d = {}
        # for i, num in enumerate(nums):
        #     if num in d and abs(i - d[num]) <= k:
        #         return True    
        #     d[num] = i
        # return False

        # alternative solution: sliding window
        window = set()
        L = 0

        for R, num in enumerate(nums):
            if R - L > k:
                window.remove(nums[L])
                L += 1

            if num in window:
                return True
            window.add(num)
        
        return False
