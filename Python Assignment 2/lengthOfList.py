##4. Write a code to ask an input from the user which is a string and display the string along
##with its length.
##Note: You cannot use len () function here.

getString = input("insert a sentence or word: ")

print("given string is: "+ getString)


##find individual letters in the given string
print("each latters in the given string are: ")
for letter in getString:
    print(letter)


##find length orf the string
print("the length of the string is: ")
len = 0
for i in getString: 
    len+= 1
    print(len)


##index = string.find("ima", "i")
##print(index)
