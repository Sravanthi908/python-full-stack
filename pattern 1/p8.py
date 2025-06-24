# output
# n=4
#         A
#       B A B
#     C B A B C
#   D C B A B C D
#     C B A B C
#       B A B
#         A

n = int(input())
char = 'A'  
for i in range(n + 1):
    print("  " * (n-i), end="")
    for j in range(i,-1,-1):
        print(chr(ord(char) + j), end=" ")
    for j in range(1, i+1):
        print(chr(ord(char) + j), end=" ")
    print()
for i in range(n -1,-1,-1):
    print("  " * (n-i), end="")
    for j in range(i,-1,-1):
        print(chr(ord(char) + j), end=" ")
    for j in range(1,i+1):
        print(chr(ord(char) + j), end=" ")

    print()
