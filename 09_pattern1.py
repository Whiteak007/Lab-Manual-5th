n = int(input("Enter no of rows: "))

for i in range(1, n + 1):
    stars = ((2*i) - 1)
    spaces = "  "*(n - i)
    each_row = spaces + "* "*stars
    print(each_row)