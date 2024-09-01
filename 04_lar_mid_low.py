n1 = int(input("Input 1st integer: "))
n2 = int(input("Input 2nd integer: "))
n3 = int(input("Input 3rd integer: "))

greater = max(n1, n2, n3)
lower = min(n1, n2, n3)
print("Greatest: ", greater)
print("Middle: ", ((n1 + n2 + n3 - greater - lower)))
print("Lowest: ", lower)
