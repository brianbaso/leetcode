from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1:
            return [nums[0]]

        # create a freq array
        c = Counter(nums)
        # {1: 3, 2: 2, 3: 1}
    
        # put the values into a new 2D array where the ith index 
        # is equal to the freq of the num
        freq = [[] for i in range(0, len(nums) + 1)]

        # [[], [], [], [], [], [], []]
        for key, val in c.items():
            freq[val].append(key)

        # loop in reverse to get k amount of most frequent elements
        ans = []
        for i in range(len(freq)-1, 0, -1):
            for num in freq[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans







        

            



