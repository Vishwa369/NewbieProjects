num = 10
n1, n2 = 0, 1

print("Fibonacci Series:", n1, n2, end=" ")
for i in range(2, num):
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    print(n3, end=" ")

print()

# Method 2 using Recursion

def fiabonacciSeries(i):
    if i <= 1:
        return i
    else:
        return (fiabonacciSeries(i - 1 ) + fiabonacciSeries(i - 2))

num = 10
if num <= 0:
    print("Please enter a Positive Number")
else:
    print("Fibonacci Series: ", end=" ")
for i in range(num):
    print(fiabonacciSeries(i), end=" ")

# Method 3 Direct formula

import math

def fibonacciSeries(phi, n):
    for i in range(0, n + 1):
        result = round(pow(phi, i) / math.sqrt(5))
        print(result, end=" ")

num = 10
phi = (1 + math.sqrt(5)/2)
fibonacciSeries(phi, num)