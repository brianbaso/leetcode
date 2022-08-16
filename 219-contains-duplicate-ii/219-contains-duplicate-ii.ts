function containsNearbyDuplicate(nums: number[], k: number): boolean {
    const map = new Map();
    const len = nums.length
    
    for (let i = 0; i < len; i++) {
        let key = map.get(nums[i])
        
        if (key) {
            map.set(nums[i], {
                "count" : key.count + 1,
                "dist"  : Math.abs(key.dist - i)
            })
            
            if (map.get(nums[i]).dist <= k) {
                return true
            } else {
                map.set(nums[i], {
                    "dist" : i
                })
            }
            
        } else {
            map.set(nums[i], {
                "count" : 1,
                "dist" : i
            })
        }
    }
    
    return false;
};