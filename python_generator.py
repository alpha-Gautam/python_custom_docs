def gen(n):
    if(n < 0):
        raise ValueError("n must be non-negative")
    
    i=1
    while(i <= n):
        yield f"Number: {i}"
        i+=1
        
        
        

for a in gen(10):
    print(a)
    

