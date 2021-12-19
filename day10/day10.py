from collections import deque

ans = 0
stack = deque()
instrings = []
corrupt = False
for x in open("input.txt"):
    instrings.append(x.strip())
    for y in x.strip():
        if y == ")":
            if stack.pop() != "(":
                ans += 3
                corrupt = True
                break
        elif y == "]":
            if stack.pop() != "[":
                corrupt = True
                ans += 57
                break
        elif y == "}":
            if stack.pop() != "{":
                corrupt = True
                ans += 1197
                break
        elif y == ">":
            if stack.pop() != "<":
                corrupt = True
                ans += 25137
                break
        else:
            stack.append(y)
    if corrupt:
        instrings.remove(x.strip())
        corrupt = False
    stack = deque()
print(ans)
scores = []
score = 0
for x in instrings:
    for y in x:
        if y == "(":
            stack.append(y)
        elif y == "[":
            stack.append(y)
        elif y == "{":
            stack.append(y)
        elif y == "<":
            stack.append(y)
        else:
            stack.pop()
    print(stack)
    while True:
        try:
            char = stack.pop()
            if char == "(":
                score *= 5
                score += 1
            elif char == "[":
                score *= 5
                score += 2
            elif char == "{":
                score *= 5
                score += 3
            elif char == "<":
                score *= 5
                score += 4
        except IndexError:
            break
    scores.append(score)
    score = 0
    stack = deque()
scores.sort()
print(len(scores))
print(scores[23])