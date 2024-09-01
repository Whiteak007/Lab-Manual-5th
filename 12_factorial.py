num = int(input("Input a number to print it's factorial: "))

fact = 1
for i in range(1, num + 1):
    fact *= i
print("Factorial = ", fact)
