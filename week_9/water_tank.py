numberOfTanks = int(input())
overflow = input().split(' ')
for i in range(len(overflow)): overflow[i] = int(overflow[i])
start = int(input())
used = []
used.append(start)
a = 1

while True:
    if overflow[start] == -1 or overflow[start] in used: 
        break
    a += 1
    used.append(overflow[start])
    start = overflow[start]


print(a)