def large_dataset():
    for i in range(101):
        yield i
for data in large_dataset():
    print(data)
