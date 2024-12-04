class Solution:
    def convertDateToBinary(self, date: str) -> str:
        nums = date.split('-')
        ans = []
        for num in nums:
            ans.append(bin(int(num))[2:])
        return ('-').join(ans)

        