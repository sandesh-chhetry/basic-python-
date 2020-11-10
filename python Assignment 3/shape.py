##5. Write a program to display the following pattern. Check also with different number of
##rows.
##     *
##    **
##   ***
##  ****
## *****

print("the shape is like this: ")
for i in range(1, 6):
    for j in range(6, 0, -1):
        if j > i:
            print(" ", end=" ")
        else:
            print("*", end=" ")
    print("")

