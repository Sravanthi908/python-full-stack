def Slug_generator(string):
    string = string.lower()
    string=list(string)
    result=""
    for i in range(0,len(string)):
        if string[i].isalnum():
            result+=string[i]
        elif string[i]==" ":
            result +="-"    
        else:
            continue    

    return result
    

title =input()
result = Slug_generator(title)
print(result)