def duplicate_numbers(arr):
    duplicate=[]
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            if arr[i]==arr[j]:
                if arr[i] not in duplicate:
                    duplicate.append(arr[i])
                    break
    return duplicate

arr=[2,3,5,4,3,2,4,7,8,9,10]

r=duplicate_numbers(arr)
print(r)