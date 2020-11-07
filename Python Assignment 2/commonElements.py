##2. Write a program that returns a list which contains common elements from two lists. Avoid
##the duplicate elements from lists.
##For example
##a = [1, 1, 3, 5, 7, 9, 9]
##b = [2, 1, 6 ,9, 2, 1, 3, 5]
##The result should be [1, 3, 5, 9]
##Note: You cannot use if-else statement here.

##given lists 
a = [1, 1, 3, 5, 7, 9, 9]
b = [2, 1, 6 ,9, 2, 1, 3, 5]

##set is that type which contain only single charecter or not duplication
##convert given list to set
print(a)
print("only single digits are: ")
convert_a_toSet =set(a)
print(convert_a_toSet)

print(b)
print("only single digits are: ")
convert_b_toSet = set(b)
print(convert_b_toSet)
