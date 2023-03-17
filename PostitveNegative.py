# Positive Negative numbers method1
num = int(input("Enter a number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

# Positive Negative numbers method2

num = int(input("\nEnter a number: "))

if num == 0:
    print("Zero")
else:
    print("Positive") if num > 0 else print("Negative")

