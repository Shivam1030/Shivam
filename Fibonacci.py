def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
n=int(input("Enter number of Fibonacci elements: "))
arr=[]
for i in range(n):
    arr.append(fibonacci(i))
print("Fibonacci series:",arr)
