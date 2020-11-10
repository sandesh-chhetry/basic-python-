##4. Write a program to display the n terms of harmonic series and their sum.
##1 + 1/2 + 1/3 + 1/4 + 1/5 ... 1/n


print("find out the sum of harmonic series")
input_ = input("insert value of n: ")
first = 0
i=1
n = int(input_)
for i in range(1,n+1):
    first = first+ (1/i)
print("the sum of {}th harmonic series is: ".format(n))    
print(first)
##    print(second)
