f = open("list.txt", "r")
a = int(f.readline())
b = int(f.readline())
c = int(f.readline())
inc = 0
for x in f:
    if b + c + int(x) > a + b + c:
        inc = inc + 1
    a = b
    b = c
    c = int(x)
print(inc)