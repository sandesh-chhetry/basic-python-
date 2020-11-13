""" ---------------------------------------------------------------------------------------------------------------------------------------------------- """
""" Exercise 2. Write a program that will convert Fahrenheit to Celsius in degrees.
 """

##function to change fehreneit to celcius
def temperature(fahrenheit):
    setCelcius = (int(fahrenheit)-32)*(5/9);
    print(str(fahrenheit)+"oF = "+ str(setCelcius)+"oC")    

##get user input value for fahrenheit
getFahrenheit = input('Insert temperature in Fahrenheit: ')

##pass input value as a parameter to the temperature function
temperature(getFahrenheit)


    
""" ---------------------------------------------------------------------------------------------------------------------------------------------------- """
""" Exercise 3. Write a program that takes seconds as time units and converts it to minutes and
seconds.
For example: 3800 seconds results in 63 minutes and 20 seconds.  """

##function to convert given second into minute and second
def timeConverter(getSecond):
    getMin = int(getSecond)//60
    getSec = int(getSecond)%60
    
    ##there was an error to concadinate string with other datatype so i convert other data type to string for better output
    print(str(getSecond) + " Seconds = "+ str(getMin) + " Minute "+ str(getSec) + " Second" )

##get user input value
getSecond = input("insert time in second: ")

##pass input value as a parameter to the timeConverter function
timeConverter(getSecond)


""" ---------------------------------------------------------------------------------------------------------------------------------------------------- """
""" Exercise 4. Consider a list of any arbitrary elements. Your code should print the length of the list
and first and fourth element of the list.  """

elements = ["1st position", "2nd position", "3rd position", "4th position", "5th position", "6th position", "7th position", "8th position", "9th position", "10th position"]
print(elements)

##function to check the position of the element
def checkPosition(position):
    print("Length of the given element is: " + str(len(elements)))
##    convert given position into integer
    _pos = elements[int(position)]
    print(str(position)+"th element of the list is : " + str(_pos ))
    
##get user input value
position = input("insert position you want to display: ")
checkPosition(position)
    


""" ---------------------------------------------------------------------------------------------------------------------------------------------------- """
""" Exercise 5. Create a list of any arbitrary elements. Your code should show the list methods as
    pop, insert and remove.  """


##list which contain some element
elements = ["1st position", "2nd position", "3rd position", "4th position", "5th position", "6th position", "7th position", "8th position", "9th position", "10th position"]
print("initial list")
print(elements)

##function to pop new element from the given list
def popElement(position):
    elements.pop(int(position))
    print("list after pop 2nd element")
    print(elements)

##function to add new element at ne required position
def addNewElement(position, newElement):
    elements.insert(position, newElement)
    print("list after insert new value as new element")
    print(elements)

##function to remove element from the given element
def removeElement(delete):
    elements.remove(delete)
    print("list after removing priviously inserted value")
    print(elements)

##pass parameter to which position pop out
popElement(2)

##pass paramater for position and value to add new element
addNewElement(8, "this is new")

##pass paramerer to remove which one to be delete
removeElement("this is new")





















