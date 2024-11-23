


def sorted_arr(arr):
    n=len(arr)

    for i in range (n-1):
        for j in range(n-i-1):
            if arr[j]<arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr

def subsequences(arr,sum):
    num_count={}
    # arr.sort(reverse=True)

    sorted_array=sorted_arr(arr)
    print(sorted_array)

    for i in sorted_array:
        if sum>=i:
            count=sum//i  # 30/4=7
            num_count[i]=count
            sum=sum-(count*i)

    return num_count

arr=[3,2,4]
sum=30
result=subsequences(arr,sum)
print(result)