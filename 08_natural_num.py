n = int(input("Enter an integer to print sum of natual numbers from 1: "))

res = 0
for i in range(1, n + 1):
    res += i 
print("Sum = ", res)