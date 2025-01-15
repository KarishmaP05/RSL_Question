# def sort_binary_array(arr):
#     low, high = 0, len(arr) - 1

#     while low < high:
#         if arr[low] == 0:
#             low += 1
#         else:
#             arr[low], arr[high] = arr[high], arr[low]
#             high -= 1
#     return arr


# arr = [1, 0,1,0,1,0,0,1]

# result = sort_binary_array(arr)
# print(result)  


def sortRray(arr):
    low=0
    high=len(arr)-1

    while low<high:
        if arr[low]==0:
            low+=1
        else:
            arr[low],arr[high]=arr[high],arr[low]
            high-=1
    return arr

arr=[1,0,1,0,0,1,0,1,0]
result=sortRray(arr)
print(result)