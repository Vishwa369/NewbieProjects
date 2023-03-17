number = 8208
num = number
digit, sum = 0, 0

length = len(str(num))
for i in range(length):
    digit = int(num % 10)
    num = num / 10
    sum += pow(digit, length)

if sum == number:
    print("Armstrong")
else:
    print("Not Armstrong")

# Method 2 Recursion

numbr = 153

no = numbr

sum = 0

length = len(str(no))

def CheckArmstrongNo(no, length, sum):
    if no == 0:
        return sum
    sum += pow(int(no % 10), length)
    return CheckArmstrongNo(no/10, length, sum)

if CheckArmstrongNo(no, length, sum) == numbr:
    print("Arms")
else:
    print("not Arms")