'''
Q1. Given: An integer N representing the total amount of money available.
Goal: Determine the maximum number of chocolates that can be purchased using N rupees, considering the following rule:
The cost of one chocolate is Rs. 3.
Three empty chocolate wrappers can be exchanged for one more chocolate.
Example:
Input: N = 15
Output: 7
Explanation:
Initially, purchase 5 chocolates using 15 rupees (5 * 3 = 15).
This leaves 5 empty chocolate wrappers.
Exchange 3 wrappers for 1 more chocolate.
Now, there are 3 wrappers (2 from the previous step + 1 from the new chocolate).
Exchange these 3 wrappers for another chocolate.
In total, 5 + 1 + 1 = 7 chocolates can be purchased
'''
def max_chocolate(Number):
    number_of_chocolate=Number//3
    Number_of_wrappers=number_of_chocolate
    while Number_of_wrappers>=3:
        new_chocolate=Number_of_wrappers//3
        number_of_chocolate+=new_chocolate
        Number_of_wrappers=Number_of_wrappers%3 + new_chocolate
    return number_of_chocolate

Number=20
print(max_chocolate(Number))