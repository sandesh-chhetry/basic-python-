##2. Ask the user for a string and print out whether this string is a palindrome or not.
##(A palindrome is a string that reads the same forwards and backwards.)




string = input("type a string to check palindrome or not: ")
##get reverse of the input string
check = string[::-1]
##print(check)
if(string == check):
    print(string+ " is palindrome.")
else:
    print(string+ " is not palindrome.")

