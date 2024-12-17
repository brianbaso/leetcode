class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L, R = 0, len(numbers)-1

        # [2,3,4,6,7,10,15] t=16

        # while L != R
        while L != R:

        # if L + R == target, return
            if numbers[L] + numbers[R] == target:
                return [L+1, R+1]

        # if L+1 + R <= target, L++
            elif numbers[L+1] + numbers[R] <= target:
                L += 1

        # else R--
            else:
                R -= 1

 
        

        

        







