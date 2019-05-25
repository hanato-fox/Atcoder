import fractions
import copy
n = int(input())
a = list(map(int, input().split()))
a_r = copy.copy(a)
a_r.reverse()
cumsum_gcd = [0]
cumsum_gcd_r = [0]
for i in range(n-1):
    cumsum_gcd.append(fractions.gcd(cumsum_gcd[i], a[i]))
    cumsum_gcd_r.append(fractions.gcd(cumsum_gcd_r[i], a_r[i]))
cumsum_gcd_r.reverse()
ans = []
for i in range(n):
    ans.append(fractions.gcd(cumsum_gcd[i], cumsum_gcd_r[i]))
print(max(ans))
