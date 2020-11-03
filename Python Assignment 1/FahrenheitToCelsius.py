##Exercise 2. Write a program that will convert Fahrenheit to Celsius in degrees.


##get data from user for temperature in fahrenheit
getFahrenheit = input("Insert temperature in Fahrenheit: ")

##there was an error to concadinate string with other datatype so i convert other data type to string for better output

setCelcius = (int(getFahrenheit)-32)*(5/9);
print(str(getFahrenheit)+"oF = "+ str(setCelcius)+"oC")    
