for i in range (5):
    print(f"outer loop {i}")
    for j in range(3):
        print(f"inner loop {j}")
    print("Back to outer loop")