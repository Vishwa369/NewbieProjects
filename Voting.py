# Voting method1

age = int(input("Enter your age: "))

if age >= 18:
    print("Vote")
else:
    print("You cannot vote")

# Voting method2

age = int(input("Enter your age: "))

result = "Vote" if age >= 18 else "You cannot vote"

print(result)
