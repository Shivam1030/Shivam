def move_zeros(arr):
    result=[]

    for x in arr:
        if x!=0:
            result.append(x)
    result+=[0]*(len(arr)-len(result))
    return result

arr=[0,1,0,3,0]
print(move_zeros(arr))