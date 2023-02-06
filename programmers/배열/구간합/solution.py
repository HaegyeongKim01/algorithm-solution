n, m = map(int, input().split())
arr = list(map(int, input().split()))
for _ in range(m):
    l, r = map(int, input().split())
    l, r = l-1, r-1
    print(sum(arr[l:r+1]))