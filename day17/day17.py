hits = 0
ans = 0
for dx in range(130):
    for dy in range(-200,300):
        ok = False
        maxy = 0
        x = 0
        y = 0
        DX = dx
        DY = dy
        for t in range(300):
            x += DX
            y += DY
            maxy = max(maxy, y)
            if DX > 0:
                DX -= 1
            DY -= 1
            if 81 <= x <= 129 and -150 <= y <= -108:
                ok = True
                break
        if ok:
            hits += 1
            ans = max(maxy, ans)
print(ans)
print(hits)