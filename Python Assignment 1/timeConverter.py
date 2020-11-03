##Exercise 3. Write a program that takes seconds as time units and converts it to minutes and
##seconds.
##For example: 3800 seconds results in 63 minutes and 20 seconds.

getSecond = input("insert time in second: ")
getMin = int(getSecond)//60
getSec = int(getSecond)%60

##there was an error to concadinate string with other datatype so i convert other data type to string for better output
print(str(getSecond) + " Seconds = "+ str(getMin) + " Minute "+ str(getSec) + " Second" )
