sports = ('Tennis', 'Basketball', 'Boxing', 'Football', 'Cricket')
players = ('Serana Williams', 'Lebron James', 'Muhammad Ali', 'Lionel Messi', 'Sachin Tendulkar')

for i in range(5):
    names = ""
    names += sports[i] + ': ' + players[i]
    print(names)