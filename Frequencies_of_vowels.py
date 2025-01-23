def frequencies_of_vowels(string):
    dict={}
    vowels=['a','e','i','o','u']
    for char in string:
        if char in dict and char in vowels:
            dict[char]+=1
        elif char in vowels:
            dict[char]=1
    return dict


string="Helloo"
result=frequencies_of_vowels(string)
print(result)