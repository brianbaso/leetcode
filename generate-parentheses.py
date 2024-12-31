class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.result = []
        def generateCombos(curr, open, close, n):
            if len(curr) == 2 * n:
                self.result.append(curr)
                return

            if close <= n and open <= n:
                if close < open:
                    generateCombos(curr + ")", open, close + 1, n)
                if open < n:
                    generateCombos(curr + "(", open + 1, close, n)
            else:
                return

        generateCombos("", 0, 0, n)
        return self.result
