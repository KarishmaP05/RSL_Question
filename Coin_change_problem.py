def sort(arr):
    n=len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j]<arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr

def coin_change(arr,sum):
    num_count={}
    sorted_array=sort(arr)
    print(sorted_array)
    for i in sorted_array:
        if sum>=i:
            count=sum//i
            num_count[i]=count
            sum=sum-(count*i)
    return num_count

arr=[2,5,1]
sum=39
result=coin_change(arr,sum)
print("result",result)