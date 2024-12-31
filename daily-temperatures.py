class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        s = []

        for i, temp in enumerate(temperatures):
            while len(s) > 0 and temp > s[-1][0]:
                lowerIdx = s.pop()[1]
                result[lowerIdx] = i - lowerIdx
                
            s.append((temp, i))

        return result
