def calculate(a, b, time_b, is_first):
    
    if is_first == True:
        start = 1
    else:
        start = len(time_b) 

    for i in range(1, len(b)):
        time_b.append(time_b[start-1] + b[i])      
        
        start += 1
        if is_first ==False:
            a.append(a[i])

    return time_b

def solution(a, b):
    m = int(input())
    q = [0]        #initialize
    time_b = [0]
    for _ in range(m):         #input question 
        q.append(int(input()))

    calculate(a, b, time_b, True)

    #input question 
    for q_num in q:
        if q_num > time_b[len(time_b)-1]:
            calculate(a, b, time_b, False)          #추가로 더 추가 
        
    #question 에 대한 답 출력 
    for q_num in q:
        for i in range(1, len(time_b)):
            if q_num > time_b[i-1] and q_num <= time_b[i]:
                print(a[i])
                break


def main():
    n = int(input())
    a , b = [""], [0]
    for _ in range(n):
        a.append(input())
    
    for _ in range(n):
        b.append(int(input()))
    
    solution(a, b)


if __name__ == "__main__":
    main()