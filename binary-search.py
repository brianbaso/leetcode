nums = [1,2,4,6,8,10]
target = 0

def binary_search(arr, x):
    lo, mid = 0, 0
    hi = len(arr) - 1

    while lo <= hi:
        mid = (hi + lo) // 2

        if arr[mid] < x:
            lo = mid + 1

        elif arr[mid] > x:
            hi = mid - 1

        else:
            return mid

    return -1

print(binary_search(nums, target))
