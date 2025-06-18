list=input().split(" ")
print (list)
keyword = input()
ra=[]
for i in list:
    if keyword in i:
        ra.append(i)
print(ra)            

