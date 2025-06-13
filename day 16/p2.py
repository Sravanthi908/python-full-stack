list1 =[11,21,23,34,34,34,54,]
max_freq =0
max_freq_element=0
freq_map={

}
for i in range(len(list1)):
    if list1[i] not in freq_map:
        freq_map[list1[i]]=1
    else:
        freq_map[list1[i]]+=1
print(freq_map)
for key in freq_map:
    if freq_map[key]>max_freq:
        max_freq=freq_map[key]        
        max_freq_element=key
print(max_freq_element)        
  