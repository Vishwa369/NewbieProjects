# Method 1
low, high = input("Enter the numbers: ").split()

for i in range(int(low), int(high)+1):
    if i % 13 == 0:
        continue
    print(i, end=" ")
