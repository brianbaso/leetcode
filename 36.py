class Solution:
    def getQuadrant(self, x: int, y: int) -> int:
        if x in range(0,3):
            if y in range(0,3):
                return 1
            elif y in range(3,6):
                return 4
            elif y in range (6,9):
                return 7
            
        elif x in range(3,6):
            if y in range(0,3):
                return 2
            elif y in range(3,6):
                return 5
            elif y in range (6,9):
                return 8

        elif x in range(6,9):
            if y in range(0,3):
                return 3
            elif y in range(3,6):
                return 6
            elif y in range (6,9):
                return 9

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # make a set for each num 1-9
        # iterate through the board and add each row, column, and quadrant
        # for each value found
        # if a value already exists in set, return false
        sets = [set() for i in range(0,10)]
        for i, row_arr in enumerate(board):
            for j, num in enumerate(row_arr):
                if num != ".":
                    val = int(num)
                    r = "r" + str(i)
                    c = "c" + str(j)
                    q = "q" + str(self.getQuadrant(i, j))
                    if r not in sets[val] and c not in sets[val] and q not in sets[val]:
                        sets[val].add(r)
                        sets[val].add(c)   
                        sets[val].add(q)
                    else:
                        return False
        return True


        
