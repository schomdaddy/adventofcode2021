import collections
f = open("input.txt")
start = f.readline().strip().split(",")
count = collections.Counter()
count.update(start)
print(count)
fish = [0,0,0,0,0,0,0,0,0]
for i in count:
    fish[int(i)] = count[i]
print(fish)
for i in range(256):
    store = fish[0]
    fish[0] = fish[1]
    fish[1] = fish[2]
    fish[2] = fish[3]
    fish[3] = fish[4]
    fish[4] = fish[5]
    fish[5] = fish[6]
    fish[6] = fish[7] + store
    fish[7] = fish[8]
    fish[8] = store
    print(i + 1, fish[0] + fish[1] + fish[2] + fish[3] + fish[4] + fish[5] + fish[6] + fish[7] + fish[8])