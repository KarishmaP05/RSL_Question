# def second_max_difference(arr):
#     # If the array has fewer than 2 elements, no differences can be calculated
#     if len(arr) < 2:
#         return "Not enough elements to calculate differences."
    
#     # Sort the array
#     arr.sort()
    
#     # Find the largest difference
#     max_diff = arr[-1] - arr[0]
    
#     # If the array has fewer than 4 unique elements, no second max difference
#     unique_values = sorted(set(arr))
#     if len(unique_values) < 2:
#         return "Not enough unique elements to calculate a second difference."
    
#     # Calculate second largest difference
#     if len(unique_values) >= 3:
#         second_diff1 = unique_values[-1] - unique_values[1]  # Max - second smallest
#         second_diff2 = unique_values[-2] - unique_values[0]  # Second max - smallest
#         second_max_diff = max(second_diff1, second_diff2)
#     else:  # Only two unique values
#         second_max_diff = unique_values[1] - unique_values[0]

#     return second_max_diff

# # Test cases
# print(second_max_difference([1, 2,4,6,9]))        # Output: 7
# print(second_max_difference([10, 20, 30]))          # Output: 10
# print(second_max_difference([1,2,4, 10]))         # Output: 8
# print(second_max_difference([4, 4, 7, 7, 10]))      # Output: 3
# print(second_max_difference([-15,-10, 0,5,20]))  # Output: 30
# print(second_max_difference([2,6]))                # Output: "Not enough unique elements to calculate a second difference."
# print(second_max_difference([4, 4, 4]))             # Output: "Not enough unique elements to calculate a second difference."
# print(second_max_difference([]))                    # Output: "Not enough elements to calculate differences."




def second_max_difference(array):
    if len(array)<2:
        print("Not enough unique elements to calculate a second difference.")

    array.sort()
    
    unique_numbers=sorted(set(array))
    if len(unique_numbers) < 2:
          return "Not enough unique elements to calculate a second difference."

    if len(unique_numbers)>=3:
        second_lagest_difference1=unique_numbers[-1]-unique_numbers[1]
        second_lagest_difference2=unique_numbers[-2]-unique_numbers[0]
        
        second_max=max(second_lagest_difference1,second_lagest_difference2)
    else:
          second_max=unique_numbers[1] - unique_numbers[0]

    return second_max


# # Test cases
print(second_max_difference([1, 2,4,6,9]))        # Output: 7
print(second_max_difference([10, 20, 30]))          # Output: 10
print(second_max_difference([1,2,4, 10]))         # Output: 8
print(second_max_difference([4, 4, 7, 7, 10]))      # Output: 3
print(second_max_difference([-15,-10, 0,5,20]))  # Output: 30
print(second_max_difference([2,6]))                # Output: "Not enough unique elements to calculate a second difference."
print(second_max_difference([4, 4, 4]))             # Output: "Not enough unique elements to calculate a second difference."
print(second_max_difference([]))                    # Output: "Not enough elements to calculate differences."





def sort(arr):
    
    n=len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j]<arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]

    return arr

def removeduplicate(sorted_array):
    arr=[]

    for i in range(len(sorted_array)):
        if sorted_array[i] in arr:
            continue
        else:
            arr.append(sorted_array[i])

    return arr

def second_max_difference(arr):
    if len(arr)<2:
        return False
    sorted_array=sort(arr)
    remove_duplicate=removeduplicate(sorted_array)
    # second_max_diff

    max_val=remove_duplicate[0]
    min_val=remove_duplicate[-1]

    second_max_val=remove_duplicate[1]
    second_min_val=remove_duplicate[-2]

    largest_diff=max_val-min_val
    second_max_diff1=second_max_val-min_val
    second_max_diff2=max_val-second_min_val

    unique_diffs = sort([largest_diff,second_max_diff1,second_max_diff2])

    unique_differences=removeduplicate(unique_diffs)

    if len(unique_differences)>2:
        return unique_differences[1]
    else:
        return False

arr=[6,2,9,4,2,4,1]
second_max=second_max_difference(arr)
print(second_max)