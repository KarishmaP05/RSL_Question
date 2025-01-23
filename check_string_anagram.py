# anagrams - we check if they contain the same characters with the same frequency.

'''
Algorithm
1. If the lengths of the two strings are different, they can't be anagrams.
2. Compute the sum of ASCII values of all characters in both strings.
3. Compute the product of ASCII values of all characters in both strings.
4 If both the sum and product match for the two strings, they are anagrams. Otherwise, they are not.

'''


def are_anagram(str1,str2):

    if len(str1) != len(str2):
        return False
    
    sum1=0
    sum2=0
    product1=0
    product2=0

    for char in str1:
        sum1+=ord(char)
        product1+=ord(char)

    for char in str2:
        sum2+=ord(char)
        product2+=ord(char)


    if sum1==sum2 and product1==product2:
        return True
    else:
        return False
    
str1="listen"
str2="silent"

if are_anagram(str1,str2):
    print( f'"{str1}" and "{str2}" are anagram ')
else:
    print( f'"{str1}" and "{str2}" are not anagram ')