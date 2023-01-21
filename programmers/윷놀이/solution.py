def main():
    rule = {1: 1, 2: 2, 3: 3, 4: 4, 0:5} # 윷 규칙 도 개 걸 윷 모
    play = list(map(int, input())).count(1) #input
    print(rule[play])
    
if __name__ == "__main__":
    main()
