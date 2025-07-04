# Program to generate the Fibonacci sequence up to n terms
n = int(input("Enter the number of terms: "))
fib = []
a, b = 0, 1
for _ in range(n):
    fib.append(a)
    a, b = b, a + b
print("Fibonacci sequence:", fib)