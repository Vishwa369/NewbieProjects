N = 10
total = 0
for i in range(1, N+1):
    total += i
print("The sum of the first", N, "numbers is:", total)

n = int(input("Enter a number: "))
sum = 0
i = 1

while i <= n:
    sum += i
    i += 1

print("The sum of the first", n, "numbers is", sum)
