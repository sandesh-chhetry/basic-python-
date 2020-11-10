##1. Write a program to display all prime numbers from 1 to 

##value from 1 to 100
print("Prime numbers between 1-100 are: ")
for i in range(1,100):
##    print(i)

##    take value from 2 to i
    for j in range(2,i):

##        check condition whether the number is divisible by other number except same number and 1
        if (i%j) == 0:
            break
    else:
##        if not divisible then print i
        print(i)
##        print(j)
