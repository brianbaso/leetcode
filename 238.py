class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1] * len(nums)
        post = [1] * len(nums)

        for i in range(len(nums)):
            if i == 0:
                pre[i] = nums[i]
            else:
                pre[i] = nums[i] * pre[i-1]
        
        for i in range(len(nums)-1, -1, -1):
            if i == len(nums)-1:
                post[i] = nums[i]
            else:
                post[i] = nums[i] * post[i+1]
        
        result = []
        for i in range(len(nums)):
            pre_val = pre[i-1] if i > 0 else 1
            post_val = post[i+1] if i < len(nums)-1 else 1
            product = pre_val * post_val
            result.append(product)
            
        return result
