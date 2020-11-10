##3. Given a string, count all lower case, upper case, digits and special symbols.

print("find out the number of capita and small letter, digit and symbols")
string  = input("enter a string: ")

##initialize a value with 0 value

upperCase = 0
lowerCase = 0
digit = 0
symbol = 0

for letter in string:
    if letter.isupper():
        upperCase = upperCase+1
    elif letter.islower():
        lowerCase=lowerCase+1
    elif letter.isdigit():
        digit = digit +1
    else:
        symbol = symbol + 1

##display the length of the letters:
print("number of capital latters: " + str(upperCase))
print("number of small latters: " + str(lowerCase))
print("number of digits: " + str(digit))
print("number of symbols: " + str(symbol))

