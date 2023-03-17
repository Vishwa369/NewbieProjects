low, high = 10, 10000

for n in range(low, high + 1):
    order = len(str(n))
    sum = 0

    temp = n

    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10

    if n == sum:
        print(n, end=" ")

# Method 2

import math

first, second = 150, 10000

def is_Armstrong(val):
    sum = 0

    arr = [int(d) for d in str(val)]

    for i in range(0, len(arr)):
        sum = sum + math.pow(arr[i], len(arr))

    if sum == val:
        print(str(val) + ", ", end="")

for i in range(first, second + 1):
    is_Armstrong(i)