import statistics

pos = open("input.txt").readline().strip().split(",")
init = 0
for i in pos:
    pos[init] = int(i)
    init += 1

mid = int(statistics.median(pos))
ans = 0
for i in pos:
    ans += abs(mid - i)
print(ans)

avg = int(statistics.mean(pos))
ans2 = 0
inc = 1
for i in pos:
    start = i
    while True:
        if i < avg:
            i += 1
        elif i > avg:
            i -= 1
        ans2 += inc
        inc += 1
        if i == avg:
            break
    inc = 1
print(ans2)