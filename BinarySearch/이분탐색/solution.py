def binary_search(start, end, arr, target):
    if start > end:
        return None
    mid = (start + end) // 2

    if arr[mid]==target:
        return mid
    #좌
    elif arr[mid] < target: 
        return binary_search(mid+1, end, arr, target)
    else:
        return binary_search(start, mid-1,arr, target)

####################################### 
#input: 
# 10 7 
# 1 3 5 7 9 11 13 15 17 19
#output:
# 4
#######################################
#input:
# 10 7
# 1 3 5 6 9 11 13 15 17 19
#output:
# 원소가 존재하지 않습니다.
#########################################
n, target = map(int, input().split())
array = list(map(int, input().split()))

res = binary_search(0, n-1, array, target)
if res:
    print(res+1)
else:
    print("원소가 존재하지 않습니다. ")
