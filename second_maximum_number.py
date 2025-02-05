
# def second_max(arr):
#     new_array=[]
#     for i in arr:
#         if i in new_array:
#             continue
#         else
# :
#             new_array.append(i)
            
            
#     print(new_array)
            
#     if len(new_array) < 2:
#         return "second maximum does not exist"
               
#     for i in range(len(new_array)):
#         for j in range(len(new_array)-i-1):
#             if new_array[j]<new_array[j+1]:
#                 new_array[j],new_array[j+1]=new_array[j+1],new_array[j]
                
#     return new_array[1]
            

# arr=[3,4]
# print(second_max(arr))




def second_max(arr):
    max=-1
    second_max=-1

    for i in range(len(arr)):
        if arr[i]> max:
            second_max=max
            max=arr[i]

        if arr[i]>second_max and arr[i]!=max:
            second_max=arr[i]

    print(second_max)      
    return second_max

arr=[51,50,49,48]
print(second_max(arr))