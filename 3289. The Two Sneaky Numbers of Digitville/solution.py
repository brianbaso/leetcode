# solution with hashmap
class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        ans, hashmap = [], {}

        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1
            if hashmap[num] > 1:
                ans.append(num)
                if (len(ans) > 1):
                    return ans
