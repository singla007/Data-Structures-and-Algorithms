for _ in range(int(input())):    
    n,k = map(int,input().split(" "))
    p = list(map(int,input().split(" ")))
    dict = {}
    for i in p:
        if k%i == 0:
            dict[i] = int(k/i)-1
    if bool(dict):
        temp = min(dict.values()) 
        res = [key for key in dict if dict[key] == temp] 
        print(res[0])
    else:
        print(-1)
