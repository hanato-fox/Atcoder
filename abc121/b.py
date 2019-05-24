n, m, c = map(int, input().split())
b = list(map(int, input().split()))
count = 0
for i in range(n):
    ai = list(map(int, input().split()))
    num = 0
    for j in range(len(ai)):
        num += ai[j] * b[j]
    if num + c >0:
        count += 1
print(count)
