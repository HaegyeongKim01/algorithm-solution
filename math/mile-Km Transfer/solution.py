def transfer():
    n, _type  = input().split()
    n = int(n)
    result = 0
    if _type == 'M':
        result = n*1.6
    else:          #K
        result = n/1.6

    result = round(result +0.0000000001, 2)            #파이썬의 round함수 특성상 0.5, 0.25 등 5로 끝나는 경우 6으로 반올림하지 않는다. 그러므로 아주 작은 수를 더한다. 
    print(result)


def main():
    t = int(input())
    for _ in range(t):
        transfer()

if __name__ == "__main__":
    main()
