def reverseArray(arr):
    # code here
    rev=[]
    for i in range(len(arr)-1,-1,-1):
        # print(i," ",arr[i])
        rev.append(arr[i])
    return rev
    
arr=[10,20,30,40] 
r=reverseArray(arr)
print(r)


def reverseArray(arr):
    # code here
    arr[:]=arr[::-1]
    return arr
    
arr=[10,20,30,40] 
r=reverseArray(arr)
print(r)