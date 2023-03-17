# Method 1
num = 123321

temp = num

reverse = 0

while temp > 0:
    remainder = temp % 10
    reverse = (reverse * 10) + remainder
    temp = temp // 10

if num == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")

# Method 2

numb = 1234432
reverse = int(str(numb)[::-1])

if numb == reverse:
    print("Palindrome!")
else:
    print("Not")

# Method 3 recursion

def recursum(numbr, rev):
    if numbr == 0:
        return rev
    remaindr = numbr % 10
    rev = (rev * 10) + remaindr

    return recursum(int(numbr/10),rev)

number = 10990
reverse = 0
reverse = recursum(number, reverse)
print("Pali") if reverse == number else print("Not Pali")