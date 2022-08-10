/**
 Do not return anything, modify nums1 in-place instead.
 */
function merge(nums1: number[], m: number, nums2: number[], n: number): void {
    if (nums2.length === 0) return
    
    let i = 0, j = 0
    let nums3 = []
    
    while (i < m && j < n) {
        if (nums1[i] <= nums2[j]) {
            nums3.push(nums1[i++])
        }
        
        else if (nums1[i] > nums2[j]) {
            nums3.push(nums2[j++])
        }
    }

    if (i >= m) {
        while (j < n) {
            nums3.push(nums2[j++])
        }
    }

    else if (j >= n) {
        while (i < m) {
            nums3.push(nums1[i++])
        }
    }

    for (let k = 0; k < m + n; k++) {
        nums1[k] = nums3[k]
    }
};