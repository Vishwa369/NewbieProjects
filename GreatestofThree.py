# Method 1
a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))

if a > b and a > c:
    print("A is greatest")
elif b > c and b > a:
    print("B is greatest")
else:
    print("C is greatest")

# Method 2

a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))

temp = a if a > b else b

result = temp if temp > c else c
print(str(result) + " is the greatest")