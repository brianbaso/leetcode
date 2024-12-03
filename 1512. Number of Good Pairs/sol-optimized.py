from collections import defaultdict

# O(n) time complexity
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        hashmap = defaultdict(int)
        # create freq table in n time
        for num in nums:
            hashmap[num] += 1

        for key, value in hashmap.items():
            if value > 1:
                for i in range(value):
                    count += i
        return count