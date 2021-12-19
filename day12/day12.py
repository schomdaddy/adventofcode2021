from collections import defaultdict, deque

E = defaultdict(list)
for x in open("input.txt"):
    a,b = x.strip().split("-")
    E[a].append(b)
    E[b].append(a)

start = ("start", set(["start"]), None)
ans = 0
stack = deque([start])
while stack:
    pos, small, double = stack.popleft()
    if pos == "end":
        ans += 1
        continue
    for y in E[pos]:
        if y not in small:
            new_small = set(small)
            if y.lower() == y:
                new_small.add(y)
            stack.append((y, new_small, double))
        elif y in small and double is None and y not in ["start", "end"]:
            stack.append((y, small, y))
print(ans)