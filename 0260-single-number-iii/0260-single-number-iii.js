/**
 * @param {number[]} nums
 * @return {number[]}
 */
var singleNumber = function(nums) {
    const len = nums.length;

    if (len === 2) {
        return [nums[0], nums[1]];
    }

    const map = new Map();
    const ans = [];

    for (let i = 0; i < len; i++) {
        map.set(nums[i], map.get(nums[i]) ? map.get(nums[i]) + 1 : 1)
    }

    for (let i = 0; i < len; i++) {
        if (map.get(nums[i]) === 1) {
            ans.push(nums[i])
        }
    } 

    return ans;
};