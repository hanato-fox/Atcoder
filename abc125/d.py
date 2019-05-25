n = int(input())
a = list(map(int, input().split()))
ans = 0
minus_count = 0
for i in range(len(a)):
    if a[i] < 0:
        minus_count += 1

if minus_count%2 == 0 or 0 in a:
    for i in range(len(a)):
        ans += abs(a[i])
else:
    for i in range(len(a)):
        ans += abs(a[i])
    a = [e for e in a if e != 0]
    a.sort(key=abs)
    ans -= abs(a[0])*2
print(ans)
