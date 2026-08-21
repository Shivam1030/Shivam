n = int(input("Enter size of the array: "))
arr = []
factorial = 1
for i in range(1,n + 1):
    arr.append(i)
    factorial*=arr[i-1]
print("Array:",arr)
print("Factorial:",factorial)
