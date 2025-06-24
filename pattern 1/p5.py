#output
#n=5
# *
# * *
# * * *
# * *
# *



n= int(input())
for i in range(n):
    if i<=n//2:
        for j in range(i+1):
            print("*",end=" ")
    if i>n//2:
        for j in range(n-i):
            print("*",end=" ")           
    print()
