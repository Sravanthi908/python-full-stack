# output
# n=6
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
n= int(input())
for i in range(n):
    for j in range(i):
        print(j+1,end=" ")
    print()    