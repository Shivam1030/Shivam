def merge_sorted_lists(list1,list2):
    i=j=0
    result=[]

    while i<len(list1)and j<len(list2):
        if list1[i]<=list2[j]:
            result.append(list1[i])
            i+=1
        else:
            result.append(list2[j])
            j+= 1

    result.extend(list1[i:])
    result.extend(list2[j:])

    return result

list1=[1,8,5,6,6,8,5,6,6,6,5,5]
list2=[7,8,5,4,4,8,8,8,9,8,4,5]
print(merge_sorted_lists(list1,list2))
