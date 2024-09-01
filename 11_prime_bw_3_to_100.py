print("Prining prime numbers from 3 to 100")

for num in range(3, 100 + 1):
    if num > 1:
        is_prime = True 
        for j in range(2, int(num ** 0.5) + 1):
            if (num % j == 0):
                is_prime = False
                break
        if is_prime:
            print(num, end=" ")
        