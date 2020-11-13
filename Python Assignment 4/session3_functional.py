""" ---------------------------------------------------------------------------------------------------------------------------------------------------- """
""" 1. Write a program to display all prime numbers from 1 to  """

##function to find prime number in a range
def findPrimeNumber(initial,final):
    for i in range(initial,final):

##    take value from 2 to i
        for j in range(2,i):

##        check condition whether the number is divisible by other number except same number and 1
            if (i%j) == 0:
                break            
        else:
##        if not divisible then print i        
            print(i)
##        print(j)

print("find prime numbers?")
initialVal = input("Insert initial value: ")
finalVal =  input("Insert final value: ")

##pass user input value to find the prime numbers
findPrimeNumber(int(initialVal),int(finalVal))


""" ---------------------------------------------------------------------------------------------------------------------------------------------------- """
""" 2. Ask the user for a string and print out whether this string is a palindrome or not.
(A palindrome is a string that reads the same forwards and backwards.)  """

##function to check whether the given string is palindrome or not
def isPalindrome(string):
##get reverse of the input string
    check = string[::-1]
    ##print(check)
    if(string == check):
        print(string+ " is palindrome.")
    else:
        print(string+ " is not palindrome.")

string = input("type a string to check palindrome or not: ")

##pass string paramater to the given function
isPalindrome("2552")

isPalindrome(string)



""" ---------------------------------------------------------------------------------------------------------------------------------------------------- """
"""6. Create a dictionary that has a key value pair of letters and the number of occurrences of
that letter in a string.
Given a string “pineapple”. The result should be as:
{“p”:3, “i”:1, “n”:1, “e”:2, “a”:1, “l”:1}
Don’t worry about the order of occurrence of letters.  """

##function to count the letters and the number in their
def countLetters(string):
    
    print("the letter with their numbers are: ")
    dictonary = {}
    for letter in string:
        dictonary[letter] = dictonary.get(letter, 0) + 1
    print(dictonary)

    
string = input("insert an string: ")
##pass input value throw parameter
countLetters(string)



















    
