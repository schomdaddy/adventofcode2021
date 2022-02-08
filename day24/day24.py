#Linear Algebra!

from z3 import *

C1 = [12, 11, 10, 10, -16, 14, 12, -4, 15, -7, -8, -4, -15, -8]
C2 = [6, 12, 5, 10, 7, 0, 4, 12, 14, 13, 10, 11, 9, 9]
C3 = [1, 1, 1, 1, 26, 1, 1, 26, 1, 26, 26, 26, 26, 26]
print(len(C1),len(C2),len(C3))

def solve(minds, smallest=False):
    solver = Solver()

    ds = [Int(f"d{i}") for i in range(14)]
    for d in ds:
        solver.add(d >= 1)
        solver.add(d <= 9)

    for i, v in enumerate(minds):
        if smallest:
            solver.add(ds[i] <= v)
        else:
            solver.add(ds[i] >= v)

    z = 0
    for d, c1, c2, c3 in zip(ds, C1, C2, C3):
        x = z % 26
        z = z / c3
        x = If(x + c1 == d, 0, 1)
        z = z * If(x == 1, 26, 1) + If(x == 1, d + c2, 0)
    solver.add(z == 0)

    if solver.check() == sat:
        m = solver.model()
        s = ""
        for d in ds:
            s += str(m.eval(d).as_long())
        return int(s)
    else:
        return None


minds = []
smallest = True
while len(minds) < 14:
    n = solve(minds, smallest=smallest)
    print(n)
    minds.append(int(str(n)[len(minds)]))
    while n is not None:
        if smallest:
            minds[-1] -= 1
            if minds[-1] == 0:
                break
        else:
            minds[-1] += 1
            if minds[-1] == 10:
                break
        n = solve(minds, smallest=smallest)
    if smallest:
        minds[-1] += 1
    else:
        minds[-1] -= 1

