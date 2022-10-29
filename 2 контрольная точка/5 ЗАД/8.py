p = int(input()) 
c = 1            
b = 1            
while True:
    v = int(input()) 
    if v == p:
        if v == 0:
            break
        c += 1
    else:
        if c > b:
            b = c
        p = v
        c = 1
    
print(b)