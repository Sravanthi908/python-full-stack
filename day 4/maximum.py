list1 = [67, 45, 78, 96, 19, 47]
brain = list1[0]
for i in range (0,len(list1)):
    print ("brain = ", brain, "and i =", i)
    if brain < list1[i]:        
        brain = list1[i]
print ("maximum number in the list is:", brain)