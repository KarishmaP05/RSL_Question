
def largest_number(array):
    current_max=array[0]
    for i in range(1,len(array)):
        if array[i]>current_max:
            current_max=array[i]
    return current_max
array=[51,50,49,48]
print(largest_number(array))

def smallest_number(array):
    current_min=array[0]
    for i in range(1,len(array)):
        if array[i]<current_min:
            current_min=array[i]
    return current_min
array=[51,50,49,48]
print(smallest_number(array))

