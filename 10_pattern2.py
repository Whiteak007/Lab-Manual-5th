n = int(input("Enter no of rows: "))

for i in range(1, n + 1):
    eachh_row = ""
    for j in range(1, i + 1):
        eachh_row += str(j) + " "
    print(eachh_row)