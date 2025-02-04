# import random
# def simulate(num=1000):
#     jar1=["R"]
#     jar2=["R"]*49 + ["B"]*50
    
#     red_count=0
    
#     for i in range(num):
#         # choose jar
#         if random.randint(0,1)==0:
#             choosen_jar=jar1
#         else:
#             choosen_jar=jar2

#             # choose marble
#         jar_size=len(choosen_jar)

#         picked_index=random.randint(0,jar_size-1)

#         choosen_marble=choosen_jar[picked_index]

#         if choosen_marble=="R":
#             red_count+=1
#         probability=red_count/jar_size
#         return probability

# probability=simulate()
# print("probability",probability)




def max_probability():
    max_prob = 0
    best_r = 0  # Best red count in one jar
    best_b = 0  # Best blue count in one jar

    for r in range(51):  
        print('r',r)# Iterate over possible red marbles (0 to 50)
        for b in range(51):
            print('b',b)# Iterate over possible blue marbles (0 to 50)
            if (r == 50 and b == 50) or (r == 0 and b == 0):
                continue  # Skip cases where both jars have the same distribution
            
            # Calculate probability formula
            prob = (r / (r + b)) + ((50 - r) / (100 - r - b))
            print("prob",prob)

            if r == 1 and b == 0:
                print(f"Probability when r=1, b=0: {prob}")

            prob /= 2  # Adjust probability as in the original formula

            if prob > max_prob:
                max_prob = prob
                best_r = r
                best_b = b

    print(f"Max probability is: {max_prob:.4f} for {best_r} red and {best_b} blue marbles in one of the jars")

# Run the function
max_probability()
