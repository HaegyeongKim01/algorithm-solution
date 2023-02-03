n = int(input())
arr = list(map(int, input().split()))

min_v = min(arr)
cnt = 0
for a in arr:
    cnt += a - min_v
    
print(cnt)