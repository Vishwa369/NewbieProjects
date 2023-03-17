# Method 1
low, high = input("Enter the numbers: ").split()

for i in range(int(low), int(high)+1):
    print(i, end=" ")
    if i % 13 == 0:
        break

# Method 2
list1 = list(map(int, input("\nNumbers: ").split()))

low = list1[0]
high = list1[1]

while low <= high:
    print(low, end=" ")
    if int(low) % 13 == 0:
        break
    low += 1