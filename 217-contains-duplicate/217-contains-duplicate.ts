function containsDuplicate(nums: number[]): boolean {
    const map = new Map();
    const len = nums.length
    
    for (let i = 0; i < len; i++) {
        let count = map.get(nums[i])
        map.set(nums[i], count ? count + 1 : 1)
        
        if (map.get(nums[i]) > 1) return true
    }
    
    return false
};