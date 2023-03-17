# Odd Even number method 1
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Given number is Even")
else:
    print("Given number is odd")

# Odd Even number method 2

num = int(input("Enter number: "))

result = "Even" if num %2 ==0 else "Odd"
print(result)

# Odd Even number method 3

def isEven(num):
    return not(num & 1)

num = int(input("Enter number: "))
print("Even num" if isEven(num) else "Odd num")