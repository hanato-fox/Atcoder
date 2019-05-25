n, m = map(int, input().split())
l_list = []
r_list = []
for i in range(m):
    l, r = map(int, input().split())
    l_list.append(l)
    r_list.append(r)
if min(r_list) - max(l_list) < 0:
    print(0)
    exit()
else:
    print(min(r_list) - max(l_list) + 1)
