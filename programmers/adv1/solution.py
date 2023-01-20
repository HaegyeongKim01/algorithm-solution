def move(s, y, x, n, m):
    x_axis = {'L': -1, 'R': +1, 'U': 0, 'D': 0}
    y_axis = {'L': 0, 'R': 0, 'U': -1, 'D': +1}
    _ = int(input())  #k no use
    t_lst = list(input())
    for t in t_lst:
        next_x, next_y = x+x_axis[t], y+y_axis[t]
        
        if next_y<0 or next_y>=n or next_x<0 or next_x>=m or s[next_y][next_x] == '#':
            continue
        x, y = next_x, next_y
        
    print(y+1, x+1)
    
def solution():
    n, m = map(int, input().split(' '))     #세로, 가로
    s =[]
    row, col = 0, 0
    for i in range(n):
        s_row = list(input())
        s.append(s_row)
        
        if '@' in s_row: 
            row, col = s_row.index('@'), i   #row, col 처음 시작 좌표 
    move(s, col, row, n, m)

def main():
    t = int(input())
    for _ in range(t):
        solution()
    
if __name__ == "__main__":
    main()
