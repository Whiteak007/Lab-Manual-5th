la = list()

print("Enter 10 random numbers: ")
for i in range(10):
    num = int(input())
    la.append(num)

search = int(input("Enter a no to search, your number present in list or not: "))

if search in la:
    print(search, ' is present')
else:
    print(search, ' is not present')
