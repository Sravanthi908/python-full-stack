posts=[
    {"user":"alice","post":"hi"},
    {"user":"bob","post":"hello"},
    {"user":"alice","post":"again"},
    {"user":"x","post":"xyz"},
    {"user":"bob","post":"again"},
]
count={}
for i in posts:
    user =i["user"]
    if user in count:
        count[user]+=1
       #count[i["user"]]=count[i["user"]]+1
    else:
        #count[i["user"]]=1
        count[user]=1
print(count)           