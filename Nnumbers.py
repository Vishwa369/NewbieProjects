# Print first N number using while loop
num1 = int(input("Enter a number: "))

i = 1
while i <= num1:
    print(str(i), end=" ")
    i += 1

# Print first N number using for loop

num2 = int(input("\nEnter a number: "))

for i in range(1, num2+1):
    print(i, end=" ")