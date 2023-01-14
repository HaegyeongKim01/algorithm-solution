def lcm(a, b):
    for i in range(max(a, b), (a * b) + 1):
        if i % a == 0 and i % b == 0:
            return i

def isPerfect():
    a, b = map(int, input().split(' '))
    return lcm(a, b) == a*b
    

def main():
    t = int(input())
    for _ in range(t):
        if(isPerfect()):
            print("Perfect")
        else:
            print("Not even close")

if __name__ == "__main__":
    main()