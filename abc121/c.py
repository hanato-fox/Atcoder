n, m = map(int, input().split())
drink = []
for i in range (n):
    a, b = map(int, input().split())
    drink.append([a, b])
drink.sort(key=lambda x:x[0])
money = 0
store = 0
for i in range(m):
    money += drink[store][0]
    drink[store][1] -= 1
    if drink[store][1] == 0:
        store += 1
print(money)
