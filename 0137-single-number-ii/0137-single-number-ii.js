/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNumber = function(nums) {
    const len = nums.length;

    if (len === 1) {
        return nums[0];
    }

    const map = new Map();

    for (let i = 0; i < len; i++) {
        map.set(nums[i], map.get(nums[i]) ? map.get(nums[i]) + 1 : 1)
    }

    for (let i = 0; i < len; i++) {
        if (map.get(nums[i]) === 1) {
            return nums[i];
        }
    } 
};