# output
#   n=4
#    4
#    4 3
#    4 3 2
#    4 3 2 1
n= int(input())
for i in range(1,n+1):
    for j in range(n,n-i,-1):
        print(j,end=" ")
    print( )    