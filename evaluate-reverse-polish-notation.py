class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        def isToken(token):
            return token == '+' or token == '-' or token == '*' or token == '/'

        s = []
        for token in tokens:
            if len(s) > 1 and isToken(token):
                b = int(s.pop())
                a = int(s.pop())

                if token == '+':
                    s.append(a + b)
                elif token == '-':
                    s.append(a - b)
                elif token == '*':
                    s.append(a * b)
                elif token == '/':
                    s.append(int(a / b))
            else:
                s.append(token)
        
        return int(s[-1])
            
