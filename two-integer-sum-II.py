
nums2 = [0,5,10,30,40,41,50,60]
nums = [0,1,2,3,4]
# if R >= target, r--
# if R < target and L+1 + R <= target L++
# else r--
target = 3

def twoIntSumII(nums: list[int], target: int) -> list[int]:
    L, R = 1, len(nums)-1

    while L != R:
        if nums[L] + nums[R] == target:
            return [L, R]
        elif nums[R] >= target:
            R -= 1
        elif nums[L+1] + nums[R] <= target:
            L += 1
        else:
            R -= 1

print(twoIntSumII(nums, target))
