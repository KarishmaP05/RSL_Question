def sort(arr):
    n=len(arr)

    for i in range (n-1):
        for j in range(n-i-1):
            if arr[j]<arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr

arr=[4,5,6,3,1,2]  # sort acending

result=sort(arr)


