def bracketMatch(text: str) -> int:
    stack = []
    for char in text:
        if len(stack) > 0 and stack[-1] == '(' and char == ')':
            stack.pop()
        else:
            stack.append(char)

    return len(stack)


t1 = bracketMatch('(())()') == 0
t2 = bracketMatch('(()') == 1
t3 = bracketMatch(')(') == 2
t4 = bracketMatch('((') == 2
t5 = bracketMatch('))') == 2
t6 = bracketMatch('') == 0

print(t1,t2,t3,t4,t5,t6)
