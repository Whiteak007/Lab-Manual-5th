num = int(input("Input a number to print it's factorial or factorial division: "))

fact = 1
fact_div = 0
for i in range(1, num + 1):
    fact *= i
    fact_div += (i/fact) 
print("Factorial = ", fact)
print("Factorial Division = ", round(fact_div, 2))

