# Program to find the largest and smallest number in a list entered by the user using a loop
nums = input("Enter numbers separated by spaces: ").split()
nums = [int(n) for n in nums]

largest = nums[0]
smallest = nums[0]
for n in nums:
    if n > largest:
        largest = n
    if n < smallest:
        smallest = n
print("Largest number:", largest)
print("Smallest number:", smallest)