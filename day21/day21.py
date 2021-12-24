p1 = 7
p2 = 3
r1 = 0
r2 = 0
r3 = 0
s1 = 0
s2 = 0
d = 1
rolls = 0
move = 0
turn = False
while s1 < 1000 and s2 < 1000:
    if not turn:
        r1 = d
        d += 1
        d %= 100
        if d == 0:
            d = 100
        r2 = d
        d += 1
        d %= 100
        if d == 0:
            d = 100
        r3 = d
        d += 1
        d %= 100
        if d == 0:
            d = 100
        move = r1 + r2 + r3
        p1 += move
        p1 %= 10
        if p1 == 0:
            p1 = 10
        s1 += p1
        turn = True
        rolls += 3
    else:
        r1 = d
        d += 1
        d %= 100
        if d == 0:
            d = 100
        r2 = d
        d += 1
        d %= 100
        if d == 0:
            d = 100
        r3 = d
        d += 1
        d %= 100
        if d == 0:
            d = 100
        move = r1 + r2 + r3
        p2 += move
        p2 %= 10
        if p2 == 0:
            p2 = 10
        s2 += p2
        turn = False
        rolls += 3
print(rolls * min(s1, s2))

