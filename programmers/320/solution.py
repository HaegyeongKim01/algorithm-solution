n = int(input())
arr = list(map(int, input().split()))

min_idx = 0
for i in range(n):
    if abs(320-arr[i]) < abs(320-arr[min_idx]):
        min_idx = i
print(min_idx+1)
