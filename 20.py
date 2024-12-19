class Solution:
    def isValid(self, s: str) -> bool:
        key = {
            "(": ")",
            "[": "]",
            "{": "}"
        }
        # iterate through s
        # if stack is empty, push char
        # else, next char is peeks closing, pop stack and continue
        stack = []
        for char in s:
            if len(stack) > 0 and stack[-1] in key and char == key[stack[-1]]:
                stack.pop()
            else:
                stack.append(char)

        return len(stack) == 0
