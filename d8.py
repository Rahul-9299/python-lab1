# Program to check if a number is a palindrome
num = input("Enter a number: ")
if num == num[::-1]:
    print(num, "is a palindrome.")
else:
    print(num, "is not a palindrome.")
