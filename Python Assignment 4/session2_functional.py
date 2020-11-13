""" ---------------------------------------------------------------------------------------------------------------------------------------------------- """
""" 1. Choose a list of your choice and find the sum of all elements of that list. For example, the
    sum of [6,9,7,5,4] is 31.
    Note: You cannot use sum () function here  """

##given defined list to find the sum
list1 = [1,2,3,3,2,1]
list2 = [5,5,5,5,5]
list3 = [4,5,7,3,8,3]
list4 = [100,503,3,65]
list5 = [5,7,3,78,9,3,3]

##print all the list to choose and show towards the UI
print('''
select one list:

list1 = [1,2,3,3,2,1]
list2 = [5,5,5,5,5]
list3 = [4,5,7,3,8,3]
list4 = [100,503,3,65]
list5 = [5,7,3,78,9,3,3]
''')

##function to add the elements of the list
def sumOfElement(chooseList):
    j=0
    for i in chooseList:
        j = i+j
    print("the sum of the  given list is: {}".format(j))


##pass paramater or the list to the sum function
choose = input("choose the list: ")
if choose == "list1":
    sumOfElement(list1)
elif choose == "list2":
    sumOfElement(list2)
elif choose == "list3":
    sumOfElement(list3)
elif choose == "list4":
    sumOfElement(list4)
elif choose == "list5":
    sumOfElement(list5)
else:
    print("invalid select choose another!!!")



""" ---------------------------------------------------------------------------------------------------------------------------------------------------- """
""" Write a program that returns a list which contains common elements from two lists. Avoid
the duplicate elements from lists.
For example
a = [1, 1, 3, 5, 7, 9, 9]
b = [2, 1, 6 ,9, 2, 1, 3, 5]
The result should be [1, 3, 5, 9]
Note: You cannot use if-else statement here. """

##given lists 
a = [1, 1, 3, 5, 7, 9, 9]
b = [2, 1, 6 ,9, 2, 1, 3, 5]

print("""
given lists are:

a = [1, 1, 3, 5, 7, 9, 9]
b = [2, 1, 6 ,9, 2, 1, 3, 5]
""")

##print(a+b)
##set is that type which contain only single charecter or not duplication
##convert given list to set

##function to combine the lists and find commpn beteen them
def commonElement(list1, list2):
    s_list1 = set(list1)
    s_list2 = set(list2)
    combine = s_list1.intersection(s_list2)
    combine_list = list(combine)
    print(" the common elements between a and b are: {}".format(combine_list))

##pass paramater diffenent lists to find the common between them
commonElement(a,b)


""" ---------------------------------------------------------------------------------------------------------------------------------------------------- """
""" Write a code to ask an input from the user which is a string and display the string along
with its length.
Note: You cannot use len () function here."""

##function to find the length  of the string using loop
def findLen(string):
    print("The given input String is: {}".format(string))

    _len = 0
    for i in string: 
        _len+= 1
    print("the length of the given string is: {}".format(_len))

inputStr = input("insert the string: ")

##pass paramater to the given function
findLen(inputStr)
