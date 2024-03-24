/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {

    const map = new Map();
    const len = nums.length;
    const expectedValues = [];

    if (nums.length === 1) {
        return 1;
    }

    for (let i = 0; i < len; i++) {
        if (!map.get(nums[i])) {
            map.set(nums[i], 1);
        }
    }

    for (let key of map.keys()) {
        expectedValues.push(key)
    }

    for (let i = 0; i < len; i++) {
        nums[i] = expectedValues[i];
    }


    return expectedValues.length;
};