# Method 1
num = 3
Flag = 0
for i in range(2,num):
    if num % i == 0:
        Flag = 1
        break
if Flag == 1:
    print("Not prime")
else:
    print("Prime")

# Method 2 optimization by break condition

num = 7
flag = 0

if num < 2:
    flag = 1
else:
    for i in range(2,num):
        if num % i == 0:
            flag = 1
            break
if flag == 1:
    print('not prime')
else:
    print('prime')

# Method 3 by N/2

num = 15
flag = 0

if num < 2:
    flag = 1
else:
    for i in range(2,int(num/2)+1):
        if num % i == 0:
            flag = 1
            break
if flag == 1:
    print('no Prime')
else:
    print('yea prime')

# Method 4 using square root

num = 91
flag = 0

if num < 2:
    flag = 1
else:
    for i in range(2,int(pow(num,0.5)+1)):
        if num % i == 0:
            flag = 1
            break
if flag == 1:
    print("No prm")
else:
    print("prm")

