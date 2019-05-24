a, b = map(int, input().split())
num_count = b - a + 1
if a % 2 == 1:
    num_count -= 1
else:
    a = 0
if b % 2 == 0:
    num_count -= 1
else:
    b = 0
if (num_count / 2) % 2 == 1:
    n = 1
else:
    n = 0
print(int(a)^int(b)^int(n))
