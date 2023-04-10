n = int(input())
cnt = 0
money = [500, 100, 50, 10]

for coin in money:
    cnt += n // coin
    n %= coin
    
print(cnt)
