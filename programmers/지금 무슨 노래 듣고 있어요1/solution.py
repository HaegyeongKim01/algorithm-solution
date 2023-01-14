def get_result(a_lst, b_lst, q_lst):
    result = []
    
    #accumulation b_lst
    for i in range(1, len(a_lst)):
        b_lst[i] = b_lst[i-1] + b_lst[i]
        
    for i in range(len(q_lst)):  #question num만큼 반복
        for j in range(len(b_lst)):
            if q_lst[i] >= b_lst[j-1]+1 and q_lst[i] <= b_lst[j]:
                result.append(a_lst[j])
    return result
        
def main():
    #input
    n = int(input())
    a_lst, b_lst, q_lst = [""], [0], []
    for _ in range(n):
        a_lst.append(input())
    for _ in range(n):
        b_lst.append(int(input()))
    m = int(input())        
    for _ in range(m):  
        q_lst.append(int(input()))
        
    #call function   
    result = get_result(a_lst, b_lst, q_lst)
    
    #print
    for r in result:        #print result 
        print(r)
        
if __name__ == "__main__":
    main()