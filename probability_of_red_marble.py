import random
def simulate(num=1000):
    jar1=["R"]
    jar2=["R"]*49 + ["B"]*50
    
    red_count=0
    
    for i in range(num):
        # choose jar
        if random.randint(0,1)==0:
            choosen_jar=jar1
        else:
            choosen_jar=jar2
        print("choosen_jar",choosen_jar)
            # choose marble
        jar_size=len(choosen_jar)
        print("jar_size",jar_size)
        picked_index=random.randint(0,jar_size-1)
        print("picked_index",picked_index)
        choosen_marble=choosen_jar[picked_index]
        print("choosen_marble",choosen_marble)
        
        if choosen_marble=="R":
            red_count+=1
        probability=red_count/num
        return probability

probability=simulate()
print("probability",probability)