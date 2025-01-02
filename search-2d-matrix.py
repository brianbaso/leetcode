class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        def columnSearch():
            lo = 0
            hi = len(matrix) - 1

            while lo <= hi:
                mid = (hi + lo) // 2

                if matrix[mid][0] > target and matrix[mid-1][0] > target:
                    hi = mid - 2

                    # if hi goes out of bounds, return the first row
                    if hi < 0:
                        return 0

                elif matrix[mid][0] < target and matrix[mid+1][0] < target:
                    lo = mid + 2
                    
                    # if lo goes out of bounds, return the last row
                    if lo > len(matrix) - 1:
                        return len(matrix) - 1

                else:
                    return mid   

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
