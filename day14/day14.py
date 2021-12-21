from collections import Counter

f = open("input.txt")
start = f.readline().strip()
c = Counter()
rules = {}
f.readline()
for x in f:
    s,e = x.split(" -> ")
    rules[s] = e.strip()
for i in range(len(start) - 1):
    c[start[i:i+2]] += 1
c2 = Counter()
for i in range(40):
    for x in c:
       c2[x[0] + rules[x]] += c[x]
       c2[rules[x] + x[1]] += c[x]
    c = c2
    c2 = Counter()
final = Counter()
for x in c:
    final[x[0]] += c[x]
final["S"] += 1
print(final)