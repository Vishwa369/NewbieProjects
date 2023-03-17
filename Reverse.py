# Easy Method
num = 12345
print(str(num)[::-1])

# Method 2

numb = 123456

#temp = numb

reverse = 0

while numb > 0:
    remainder = numb % 10
    reverse = (reverse * 10) + remainder
    numb = numb // 10

print(reverse)

# Method Recursion

def recursum(number, reverse):
    if number == 0:
        return reverse
    remainder = number % 10
    reverse = (reverse * 10) + remainder
    return recursum(int(number//10), reverse)

numbr = 987654321
reverse = 0
print(recursum(numbr, reverse))