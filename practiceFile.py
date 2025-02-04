# #Print String Without Repeating Characters
# def removeDuplicate(string):
#     res=''

#     for char in string:
#         if char in res:
#             continue
#         else:
#             res+=char

#     return res
# string="helper"
# print(removeDuplicate(string))




# Given a time in hours and minutes, calculate the smaller angle formed between the hour and minute hands of a clock

# def minute_angle(minute):
#     return 6*minute


# def hour_angle(hour,minute):
#     hour=hour%12
#     return 30*hour+0.5*minute

# def angle(hour,minute):

#     minuteangle=minute_angle(minute)
#     hourangle=hour_angle(hour,minute)

#     anglediff=hourangle-minuteangle

#     if anglediff>180:
#         anglediff=360-anglediff
#     if anglediff<0:
#         anglediff=-anglediff
#     return anglediff

# hour=3
# minute=30
# print(angle(hour,minute))



# Sort Array of 0s and 1s Using One Loop
# def sortedarr(arr):
#     n=len(arr)

#     low=0  
#     high=n-1

#     while low<high:
#         if arr[low]==0:
#             low+=1
            
#         else:
#             arr[low],arr[high]=arr[high],arr[low]
#             high-=1
#     return arr

# arr=[1,0,0,1,1,0]
# print(sortedarr(arr))


# Occurrence of Characters in a String
# def string_occurance(string):
#     char_count={}

#     for char in string:
#         if char in char_count:
#             char_count[char]+=1
#         else:
#             char_count[char]=1

#     return char_count

# string="programming"
# print(string_occurance(string))


#  Second Maximum Difference in Array



# def sort(arr):

#     n=len(arr)
#     for i in range(n-1):
#         for j in range(n-i-1):
#             if arr[j]<arr[j+1]:
#                 arr[j],arr[j+1]=arr[j+1],arr[j]

#     return arr

# def removeduplicate(sorted_array):
#     arr=[]

#     for i in range(len(sorted_array)):
#         if sorted_array[i] in arr:
#             continue
#         else:
#             arr.append(sorted_array[i])

#     return arr

# def second_max_difference(arr):
#     if len(arr)<2:
#         return False
#     sorted_array=sort(arr)
#     remove_duplicate=removeduplicate(sorted_array)
#     # second_max_diff

#     max_val=remove_duplicate[0]
#     min_val=remove_duplicate[-1]

#     second_max_val=remove_duplicate[1]
#     second_min_val=remove_duplicate[-2]

#     largest_diff=max_val-min_val
#     second_max_diff1=second_max_val-min_val
#     second_max_diff2=max_val-second_min_val

#     unique_diffs = sort([largest_diff,second_max_diff1,second_max_diff2])

#     unique_differences=removeduplicate(unique_diffs)

#     if len(unique_differences)>2:

#         return unique_differences[1]
#     else:
#         return False

# arr=[6,2,9,4,2,4,1]
# second_max=second_max_difference(arr)
# print(second_max)



# Sum of Digits of an Integer
# def sum_of_integer(number):
#     num=str(number)
#     sum=0

#     for i in num:
#         sum+=int(i)

#     return sum


# number=34321
# print(sum_of_integer(number))


# First Non-Repeated Character in String

# def first_non_repeating_character(string):

#     char_count={}
#     res=[]

#     for char in string:
#         if char in res:
#             char_count[char]+=1
#         else:
#             res.append(char)
#             char_count[char]=1

#     # return char_count

#     for char in string:
#         if char_count[char]==1:
#             return char

  
            
# string="hello"
# print(first_non_repeating_character(string))


# Check if a Number is a Fibonacci Member

# def is_perfect_square(num):
#     i=0
#     while i*i<=num:
#         if i*i==num:
#             return True
#         i+=1
#     return False

# def is_fibonacci(number):
#     # 5*n*n+4  or 5*n*n-4

#     if is_perfect_square(5*number*number+4)  or is_perfect_square(5*number*number-4):
#         return f"{number} is member of fibonacci series"
#     else:
#         return f"{number} is not member of fibonacci series"

# number=13
# print(is_fibonacci(number))


#  Given a set of coin denominations and a total value, find the minimum number of coins required to make the given value. Assume you have an infinite number of coins for each denomination.

# def coin_change(coins,value):
#     coin_count={}
#     sortarray=sorted(coins,reverse=True)  # 5,2,1
#     print("sortarray",sortarray)

#     for coin in sortarray:
#         print("coin",coin)
#         count=value//coin
#         print(count)
#         coin_count[coin]=count
#         value=value-(coin*count)
#     return coin_count


# coins = [1, 2, 5]
# value = 11
# print(coin_change(coins,value))


# there is a house which have 7 compounds where every compund have 1 gatekeeper and I have few chocolates. I have to pass the compound by giving half of my chocolates to every gatekeeper and in return he will give me 1 of the chocolates so minimum how many chocolates I have to keep to enter in house so that after going inside house i will be left with 2 chocolates?
# def total_chocolate(compounds,final_choco):
#     total=final_choco # start from back

#     for i in range(compounds):
#         total=(total-1)*2
#     return total
# compounds=7
# final_choco=2
# print(total_chocolate(compounds,final_choco))



# Function to print full pyramid pattern
# def full_pyramid(n):
#     for i in range(1, n + 1):
#         # Print leading spaces
#         for j in range(n - i):
#             print("", end="")
        
#         # Print asterisks for the current row
#         for k in range(1, i+1):
#             print(i, end="")
#         print()
   
# full_pyramid(5)






#coin change
def sort(coins):
    n=len(coins)
    for i in range(n):
        for j in range(n-i-1):
            if coins[j]<coins[j+1]:
                coins[j],coins[j+1]=coins[j+1],coins[j]
    return coins




# def coin_change(coins,value):
#     coin_count={}
#     # sort coins in descending
#     sortedcoins=sort(coins)
#     print("sortedcoins",sortedcoins)
#     for coin in sortedcoins:
#         if value>=coin:
#             count=value//coin
#             coin_count[coin]=count
#             value=value-(coin*count)
#     print("coin_count",coin_count)
#     return coin_count



# coins=[2,1,5]
# value=23
# coin_change(coins,value)

def index(arr):
    sorted_array=[]

    for i in range(len(arr)):
        sorted_array.append((arr[i],i))

    n=len(sorted_array)

    for i in range(n):
        for j in range(n-i-1):
            if sorted_array[j][0]<sorted_array[j+1][0]:
                sorted_array[j],sorted_array[j+1]=sorted_array[j+1],sorted_array[j]

    print(sorted_array)

    sorted_indices=[]

    for i in range(n):
        sorted_indices.append(sorted_array[i][1])
    return sorted_indices


arr=[5,6,8,4,3]  # sort= 8,6,5,4,3  => 2,1,0,3,4


print(index(arr))