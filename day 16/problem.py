list =[11,21,23,34,34,34,54,]
max_freq =0
max_freq_element=0
for i in range(0,len(list)):
    count =1
    for j in range(i+1,len(list)):
        if list[i]==list[j]:
            count+=1
    if max_freq<count:
        max_freq=count
        max_freq_element=list[i]
print(max_freq_element)        

