def sort(arr):
    indexed_arr = []
    for i in range(len(arr)):
        indexed_arr.append((arr[i], i))
    
    n=len(indexed_arr)

    for i in range (n):
        for j in range(0,n-i-1):
            if indexed_arr[j][0]<indexed_arr[j+1][0]:
                indexed_arr[j],indexed_arr[j+1]=indexed_arr[j+1],indexed_arr[j]

    sorted_indices=[]
    for i in range(n):
        sorted_indices.append(indexed_arr[i][1])
    return sorted_indices

arr=[100, 150, 98, 99, 101]  # sort acending

result=sort(arr)
print("sorted_indeices",result)