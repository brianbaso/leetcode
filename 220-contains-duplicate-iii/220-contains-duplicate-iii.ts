function containsNearbyAlmostDuplicate(nums: number[], k: number, t: number): boolean {
    const len = nums.length
    for (let i = 0; i < len; i++) {
        for (let j = 1; j <= k; j++) {
            if (Math.abs(nums[i] - nums[i+j]) <= t) return true
        }
    }
    
    return false
};