n = int(input())
arr = list(map(int, input().split()))

dup_arr = arr
for a in arr:
    small_cnt, big_cnt = 0, 0
    
    sorted(dup_arr)
    for i in range(len(dup_arr)):
        if dup_arr[i] < a :
            small_cnt += 1
        elif dup_arr[i] > a:
            big_cnt += 1
    print(small_cnt, big_cnt )