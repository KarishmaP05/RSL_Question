
# def maxprofit(prices):
#     n=len(prices)
#     transaction=[]
#     max_profit=0
    
#     for i in range(1,n): #1,2,3,4,5,6
#       print(i)
#       if prices[i]>prices[i-1]: # 180>100, 260>180, 310-260, 40>310, 535>40 , 695>535
#           buy_day=i-1 #0=100  180  310  535  695>535
#           sell_day=i #1= 180  260  260   40
#           profit=prices[sell_day]-prices[buy_day]   # 80+80+50+495+ 160
#           transaction.append((buy_day,sell_day,profit))

#           max_profit+=profit  # 210+495+160

#     # print(max_profit)
#     return max_profit,transaction
    
# prices=[100, 180, 260, 310, 40, 535, 695]

# max_profit,transaction=maxprofit(prices)

# def print_transactions(prices,transaction):
#     for buy,sell,profit in transaction:
#         print(f"buy stock on day {buy} in ruppees {prices[buy]} and sell stock on day {sell} in rupees {prices[sell]}, profit is {profit}")

# print("for prices",prices)

# print_transactions(prices,transaction)
# print(f"max_profit is {max_profit}")


print("second!!!!!!!!!!!11")




def maxprofit(prices):
    n=len(prices)
    transaction=[]
    max_profit=0
    i=0
    while i<n-1: # 0, 7
        while i<n and prices[i]>prices[i+1]:  # buy stock  1000>180 , 180>100, 100>260
            i+=1
        if i==n-1:
            break
        buy=i  #2(100)
        i+=1 # 3

        while i <n and prices[i]>prices[i-1]: # sell stock
            i+=1
        sell = i-1
        profit=prices[sell]-prices[buy]
        max_profit+=profit
    return max_profit,transaction
prices=[1000, 180, 100,260, 310, 40, 535, 695]

max_profit,transaction=maxprofit(prices)


def print_transactions(prices,transaction):
    for buy,sell,profit in transaction:
        print(f"buy stock on day {buy} in ruppees {prices[buy]} and sell stock on day {sell} in rupees {prices[sell]}, profit is {profit}")

print("for prices",prices)

print_transactions(prices,transaction)
print(f"max_profit is {max_profit}")



# Overall Time Complexity: O(n)




















# # Function to calculate the maximum profit
# def maximumProfit(prices):
#     n = len(prices)
#     lMin = prices[0]  # Local Minima
#     lMax = prices[0]  # Local Maxima
#     res = 0
  
#     i = 0
#     while i < n - 1:
      
#         # Find local minima
#         while i < n - 1 and prices[i] >= prices[i + 1]:
#             i += 1
#         lMin = prices[i]
        
#         # Local Maxima
#         while i < n - 1 and prices[i] <= prices[i + 1]:
#             i += 1
#         lMax = prices[i]
      
#         # Add current profit
#         res += (lMax - lMin)
  
#     return res

# # Driver Code
# if __name__ == "__main__":
#     prices = [100, 180, 260, 310, 40, 535, 695]
#     print(maximumProfit(prices))