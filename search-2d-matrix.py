class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def columnSearch():
            if len(matrix) == 1:
                return 0

            lo = 0
            hi = len(matrix) - 1

            while lo <= hi:
                mid = (hi + lo) // 2
                print(mid)

                if matrix[mid][0] > target:
                    if mid == 0:
                        return 0
                    if matrix[mid - 1][-1] < target:
                        return False
                    hi = mid - 1

                elif matrix[mid][0] < target:
                    if matrix[mid][-1] >= target:
                        return mid
                    else:
                        lo = mid + 1
                else:
                    return mid
                
                if lo == hi:
                    return lo
            
        def rowSearch(column):
            print(column)
            lo = 0
            hi = len(matrix[column]) - 1

            while lo <= hi:
                mid = (hi + lo) // 2

                if matrix[column][mid] > target:
                    hi = mid - 1
                elif matrix[column][mid] < target:
                    lo = mid + 1
                else:
                    return True
            
            return False

        col = columnSearch()
        result = rowSearch(col)
        return result
