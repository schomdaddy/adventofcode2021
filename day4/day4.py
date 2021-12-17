import sys

f = open("input.txt")
line = f.readline().strip()
f.readline()
call = line.split(",")
print(call)
cards = []
card = []
for x in f:
    if x.strip() == "":
        cards.append(card)
        card = []
    else:
        line = x.strip()
        card.append(line.split(" "))
for c in cards:
    for x in c:
        while True:
            try:
                x.remove("")
            except ValueError:
                break


def checkBingo(bcard):
    for x in range(5):
        for y in range(5):
            if bcard[x][y] == "-1":
                if y == 4:
                    return True
            else:
                break
    for x in range(5):
        for y in range(5):
            if bcard[y][x] == "-1":
                if y == 4:
                    return True
            else:
                break
    if bcard[0][0] == bcard[1][1] == bcard[2][2] == bcard[3][3] == bcard[4][4]:
        return True
    if bcard[4][0] == bcard[3][1] == bcard[2][2] == bcard[1][3] == bcard[0][4]:
        return True
    return False


def getScore(bcard, called):
    ret = 0
    for x in range(5):
        for y in range(5):
            if bcard[x][y] != "-1":
                ret += int(bcard[x][y])
    for x in range(5):
        for y in range(5):
            bcard[x][y] = "-2"
    return (ret * int(called))


for n in call:
    for c in cards:
        for x in range(5):
            for y in range(5):
                if c[x][y] == n:
                    c[x][y] = "-1"
                    if checkBingo(c):
                        print(getScore(c, n))
