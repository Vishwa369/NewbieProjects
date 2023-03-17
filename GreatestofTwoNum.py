# Method 1
first = int(input("Enter a 1st number: "))
second = int(input("Enter a 2nd number: "))

if first == second:
    print("Both are equal")
elif first > second:
    print(str(first) + " is Greater")
else:
    print(str(second) + " is Greater")

# Method 2

first = int(input("Enter a 1st number: "))
second = int(input("Enter a 2nd number: "))

if first == second:
    print("Both are equal")
else:
    result = first if first > second else second
    print(result)

# Method 3

first = int(input("Enter a 1st number: "))
second = int(input("Enter a 2nd number: "))

if first == second:
    print("Both are equal")
else:
    result1 = max(first, second)
    print(result1)