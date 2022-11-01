n = int(input())
ans = [0] * n

while (0 in ans):
    print(ans)
    l = n-1
    while (ans[l] != 0):
        ans[l] = 0
        l -= 1
    ans[l] = 1
print(ans)