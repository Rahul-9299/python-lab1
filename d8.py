122# Program to check if a number is a palindrome

# Get user input
num = input("Enter a number: ")
if num == num[::-1]:
    print(num, "is a palindrome.")
else:
    print(num, "is not a palindrome.")