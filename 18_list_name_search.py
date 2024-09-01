la = list()

print("Enter 10 random names: ")
for i in range(10):
    name = input()
    la.append(name)

search = input("Enter a no to search, your number present in list or not: ")

if search in la:
    print(search, ' is present')
else:
    print(search, ' is not present')
