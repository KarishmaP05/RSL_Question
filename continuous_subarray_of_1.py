def conti(arr):
    current_len=0
    max_len=0
    
    for i in arr:
        if i==1:
            current_len+=1
            max_len=max(max_len,current_len)
        else:
            current_len=0
            
    print(max_len) 
    final=[]
    for i in range(max_len):
        final.append(1)
    print(final)
            
            

arr=[0,1,1,1,0,1,1,1,1]
conti(arr)