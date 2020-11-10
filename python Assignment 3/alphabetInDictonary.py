##6. Create a dictionary that has a key value pair of letters and the number of occurrences of
##that letter in a string.
##Given a string “pineapple”. The result should be as:
##{“p”:3, “i”:1, “n”:1, “e”:2, “a”:1, “l”:1}
##Don’t worry about the order of occurrence of letters.


string = input("insert an string: ")
print("the letter with their numbers are: ")
dictonary = {}
for letter in string:
    dictonary[letter] = dictonary.get(letter, 0) + 1
print(dictonary)

