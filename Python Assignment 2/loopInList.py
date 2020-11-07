##3. Suppose you have a list [1, 5, 7, 12 ,15]
##Print each number using loop. Also, print the square of each number using loop.

list = [1, 5, 7, 12, 15]
##print all elements of list
for i in list:
    print(i)

for i in list:
##    get square of each elements of list
    square = i**2
    print("the square of "+str(i) +" is: " + str(square))
