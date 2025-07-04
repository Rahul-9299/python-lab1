# Program to find all Armstrong numbers between 100 and 999 using loops
for num in range(100, 1000):
    temp = num
    sum_cubes = 0
    while temp > 0:
        digit = temp % 10
        sum_cubes += digit ** 3
        temp //= 10
    if sum_cubes == num:
        print(num)