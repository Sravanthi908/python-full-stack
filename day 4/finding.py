list1 = [34, 78, 45, 96, 23]
x = int(input())
for i in range (0, len(list1)):
    if x == list1[i]:
        print ("number found")
    else:
        print ("number not found")
        break