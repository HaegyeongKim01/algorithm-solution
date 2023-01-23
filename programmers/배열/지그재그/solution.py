arr1 = list(map(int, input().split(' ')))
arr2 = list(map(int, input().split(' ')))

cnt = 0

for i , j in zip(arr1, arr2):
    print(i, j, end=" ")
    cnt += 1

if len(arr1) > len(arr2):
    for k in range(cnt, len(arr1)):
        print(arr1[k], end = " ")
elif len(arr1) < len(arr2):
    for k in range(cnt, len(arr2)):
        print(arr2[k], end = " ")
