def count_char(string):
    char_set = set(string)  # create a set of unique characters
    for char in char_set:  # iterate over the unique characters
        print(char, ' occurs ', string.count(char), ' times.')

string = input("Enter a string: ")
count_char(string)