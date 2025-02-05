def pair(arr, sum_value):
    low = 0
    high = len(arr) - 1
    result = []

    # Sort the array to ensure we get unique pairs and avoid duplicates
    arr.sort()
    
    # Find unique pairs whose sum equals sum_value
    while low < high:
        current_sum = arr[low] + arr[high]
        
        if current_sum == sum_value:
            result.append((arr[low], arr[high]))  # Store pair
            low += 1
            high -= 1
        elif current_sum < sum_value:
            low += 1
        else:
            high -= 1


    return result

def find_combinations(arr, sum_value):
    results = []
    
    # Try combinations of 3 elements as well
    for i in range(len(arr) - 2):
        low = i + 1
        high = len(arr) - 1
        while low < high:
            current_sum = arr[i] + arr[low] + arr[high]
            if current_sum == sum_value:
                results.append((arr[i], arr[low], arr[high]))  # Store triplet
                low += 1
                high -= 1
            elif current_sum < sum_value:
                low += 1
            else:
                high -= 1
                
    return results

def find_single_elements(arr, sum_value):
    result = []
    for num in arr:
        if num == sum_value:
            result.append((num,))  # Add as a single-element tuple
    return result

def pair_sum(arr, sum_value):
    pair_results = pair(arr, sum_value)
    print("pair",pair_results)
    combination_results = find_combinations(arr, sum_value)
    print("combination_results",combination_results)
    single_element_results = find_single_elements(arr, sum_value)
    print("single_element_results",single_element_results)
    
    # Combine results and print output as per the desired format
    output = pair_results + combination_results + single_element_results
    for res in output:
        print("res",res)

# Example usage
arr = [1, 2, 3, 4, 5, 6,7,8]
sum_value = 10
pair_sum(arr, sum_value)









# def find_subsequences_with_sum(arr, target, index=0, current=[], current_sum=0):
#     # Base case: If we reach the end of the array
#     if index == len(arr):
#         if current_sum == target:
#             print(current)  # Print the valid subsequence
#         return
    
#     # Include the current element
#     find_subsequences_with_sum(arr, target, index + 1, current + [arr[index]], current_sum + arr[index])
    
#     # Exclude the current element
#     find_subsequences_with_sum(arr, target, index + 1, current, current_sum)

# # Example usage
# arr = [1, 2, 3, 4, 5]
# target_sum = 10
# find_subsequences_with_sum(arr, target_sum)
