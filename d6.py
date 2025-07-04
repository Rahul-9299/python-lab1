# Program to accept 10 integers and count positives, negatives, and zeros
positives = 0
negatives = 0
zeros = 0

for _ in range(10):
    num = int(input("Enter an integer: "))
    if num > 0:
        positives += 1
    elif num < 0:
        negatives += 1
    else:
        zeros += 1

print("Positive numbers:", positives)
print("Negative numbers:", negatives)
print("Zeros:", zeros)