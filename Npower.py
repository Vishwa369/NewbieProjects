'''# Method 1
base = float(input("Enter Base number: "))
expo = float(input("Enter Expo number: "))
temp = pow(base,expo)

print(temp)'''

# Method 2

base = float(input("Enter Base number: "))
expo = float(input("Enter Expo number: "))

result = 1
while expo != 0:
    result *= base
    expo -= 1

print(result)
print(expo)