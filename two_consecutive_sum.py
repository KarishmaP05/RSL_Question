def consecutive(arr):
    max_sum=0
    max_pair=None
    for i in range(len(arr)-1):
        if arr[i]+arr[i+1] > max_sum:
            max_sum=arr[i]+arr[i+1]
            max_pair=(arr[i],arr[i+1])
            
    print(max_sum,max_pair)
            
        



arr=[15,7,6,28,9,4,2,24]
consecutive(arr)