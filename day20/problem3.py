user_list=[
    {"name":"sam","id":1,}
    
]

list=[]
n=int(input())
for i in range(n):

    new_dict = {}
    new_dict["name"] = input()
    new_dict["id"] = int(input())
    user_list.append(new_dict)

print(user_list)
search=input()
filter_list=[]
for i in user_list:
    if search.lower() in i["name"].lower():
        filter_list.append(i)
print(filter_list)        





