for _ in range(int(input())):    
    s = input()
    p = input()
    sorteds = ''
    l =len(s)
    for i in range(l):
        sorteds += min(s)
        s= s.replace(min(s),'',1)
    def reverse(string): 
        string = string[::-1] 
        return string 
    
    strrev = reverse(sorteds)
    for i in p:
        sorteds= sorteds.replace(i,'',1)
    strrev = reverse(sorteds)
    prev = reverse(p)
    out = ''
    check = 1
    for i in strrev:
        if i<=prev[-1] and check:
            out+=prev
            check = 0
            if i==prev[-1] or i<prev[-1]:
                out+=i
        else:
            out+=i
    print(reverse(out))
