# solution with set
class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        ans, s = [], set()

        for num in nums:
            if num in s:
                ans.append(num)
                if len(ans) > 1:
                    return ans
            else:
                s.add(num)