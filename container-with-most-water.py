class Solution:
    def maxArea(self, height: List[int]) -> int:
        # start with L and R pointer
        # calculate area (R-L) * min(height1, height2)
        # if area > max, max = area
        # if R > L, L++ else R--
        L, R = 0, len(height)-1
        max_area = 0
        while L < R:
            area = (R - L) * min(height[L], height[R])
            if area > max_area:
                max_area = area
            if height[R] > height[L]:
                L += 1
            else:
                R -= 1
        return max_area
