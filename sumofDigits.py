# Method 1
a = "12345"

print(a[::-1])

# Method 2

num = 123456
temp = num
reverse = 0

while num > 0:
    remainder = num % 10
    reverse = (reverse * 10) + remainder
    num = num // 10

print(reverse)

# Method 3

def recursum(number, reverse):
    if number == 0:
        return reverse
    remainder = int(number%10)
    reverse = (reverse*10) + remainder
    return recursum(int(number/10),reverse)

num = 1234
reverse = 0
print(recursum(num,reverse))

