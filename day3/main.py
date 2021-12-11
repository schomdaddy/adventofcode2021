list = [0,0,0,0,0,0,0,0,0,0,0,0]
increment = 0
spot = 0
gamma = 0
epslon = 0
f = open("input.txt")
for x in f:
    increment += 1
    for y in x:
        if y == '1':
            list[spot] += 1
        spot += 1
    spot = 0
print(list)
print(increment)
for z in list:
    if z/increment > 0.5:
        print(2 ** (11 - spot))
        gamma += 2 ** (11 - spot)
    else:
        print(2 ** (11 - spot))
        epslon += 2 ** (11 - spot)
    spot += 1
print(gamma, epslon)
print(gamma * epslon)
